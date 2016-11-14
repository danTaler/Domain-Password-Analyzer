#!/usr/bin/env python

import os
from flask import Flask, request, redirect, url_for
from flask import render_template, session
from flask import send_from_directory
from werkzeug import secure_filename

''' Import CLASSES '''
from passwordAudit import CLASS_passwordAudit
from uploadedFiles import CLASS_upload_files_edit
from summary       import CLASS_summary
from hackedAccount import class_haveibeenhacked



'''
    General Configurations
    -----------------------------------------
'''
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt'])
app.secret_key = os.urandom(24)

''' global Classes '''
class_upload_files      = CLASS_upload_files_edit()
class_summary           = CLASS_summary()
class_pass              = CLASS_passwordAudit()


'''
    / route -> homepage -> upload files
------------------------------------------------
'''
@app.route('/')
def main():

    return render_template('uploadFiles.html')


'''
     /uploads
------------------------------------------------
        inputs: NTDS, Cracked file, Client name
        Actions:
            1. Get inputs
            2. Check file extensions
            3. Secure files
            4. Store files in /uploads/client....
'''
@app.route('/uploads', methods=['POST'])
def uploadedFile():

    MSG_NTDS=MSG_hash_pass=MSG_pass=''

    ''' Session for client name '''
    '''--------------------------------------------------'''
    if request.form['client_name']:
        full_company_name = request.form['client_name']            # Company.com.au
        a = full_company_name.strip().split('.')

        clientName = a[0]                                # Company = a[0]

        session['client_name'] = clientName


    ''' Saving NTDS file  '''
    '''--------------------------------------------------'''
    if request.files['NTDS']:
        file_NTDS = request.files['NTDS']
        if file_NTDS and allowed_file(file_NTDS.filename):
            filename = secure_filename(file_NTDS.filename)

            ''' Storing the file on local /uploads/ folder '''
            file_NTDS.save(os.path.join(app.config['UPLOAD_FOLDER'],clientName+'_NTDS_'+filename))

            ''' Upload files class. Processing the files into Lists/Dictionary.
                Calling these functions once only !!! '''
            client_name = class_upload_files.show_client_name(session['client_name'])

            ''' storing the NTDS file into list '''
            class_upload_files.NTDS_into_List()


            MSG_NTDS = 'OK'
            session['NTDS'] = True

    ''' The Password Only File '''
    '''--------------------------------------------------'''
    if request.files['CRACKED_PASSWORDS']:
        CRACKED_PASSWORDS = request.files['CRACKED_PASSWORDS']
        if CRACKED_PASSWORDS and allowed_file(CRACKED_PASSWORDS.filename):
            filename = secure_filename(CRACKED_PASSWORDS.filename)

            ''' Storing the file on local /uploads/ folder '''
            CRACKED_PASSWORDS.save(os.path.join(app.config['UPLOAD_FOLDER'], clientName+'_passwords_'+filename))


            client_name = class_upload_files.show_client_name(session['client_name'])

            ''' storing the Password file into list '''
            class_upload_files.PASSWORDS_into_list()


            MSG_pass = 'OK'
            session['passwords'] = True

    ''' The Hash-Password File   '''
    if request.files['hash_password']:
        hash_password = request.files['hash_password']
        if hash_password and allowed_file(hash_password.filename):
            filename = secure_filename(hash_password.filename)

            ''' Storing the file on local /uploads/ folder '''
            hash_password.save(os.path.join(app.config['UPLOAD_FOLDER'], clientName+'_hash_pass_'+filename))


            ''' storing the Hash:Password file into list '''
            class_upload_files.Hash_Pass_into_list()

            ''' Merging the Hash:Password with NTDS into User:Hash:Password'''
            class_upload_files.merge_ntds_with_hashPass_file()
            #client_name = class_pass.show_client_name(session['client_name'])


            MSG_hash_pass = 'OK'

    return render_template('uploadFiles.html', MSG_NTDS=MSG_NTDS,MSG_pass=MSG_pass,
                                                client_name=clientName,MSG_hash_pass=MSG_hash_pass)


#
# Function to verify filename
# ----------------------------------------------

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



'''
    Summary Page
    -------------------------------------------------------
'''
@app.route('/summary')
def summary():

    ''' If session value (client name) is empty, render page without data
    -----------------------------------------------------------------------'''
    if session.values() == []:

          client_name = 'no client data found -> upload new data'

          return render_template('Summary.html',client_name=client_name)

    else:
        ''' There is a client session '''
        ''' need to make sure data loads only once!!! '''

        if not 'NTDS' in session:
            print 'no ntds !!!'

            return render_template('Summary.html')

        if 'NTDS' in session:
            print ' ntds in session !!!'

            client_name = session['client_name']

            ''' Getting the NTDS and password list from File Upload Class '''
            ntds_list                       = class_upload_files.get_ntds_list()
            password_list                   = class_upload_files.get_password_list()


            ''' == Functions of Summary Class == '''
            numberOfUsers                   = class_summary.number_of_username_NTDS(ntds_list)

            numberOfLM                      = class_summary.number_of_LMs(ntds_list)

            usersContainAdmin               = class_summary.users_contain_admin(ntds_list)
            users_contain_test              = class_summary.users_contain_test(ntds_list)
            users_contain_companyName       = class_summary.users_contain_companyName(ntds_list, client_name)
            users_contain_serviceAccount    = class_summary.users_contain_serviceAccount(ntds_list)



            ''' == Functions of Password Class == '''

            ''' Calling password class functions once only !!! '''
            class_pass.password_length(password_list)
            class_pass.most_common_password(password_list)


            password_length                 = class_pass.get_dict_password_length()
            get_total_passwords             = class_pass.total_passwords(password_list)

            Not_Cracked                     = (numberOfUsers - get_total_passwords)

            most_common_pass                = class_pass.get_dict_most_common_pass()


            ''' == class_haveibeenhacked == '''

            #pwn = class_haveibeenhacked()
            #pwn.haveibeenhacked()

            return render_template('Summary.html',client_name=client_name, numberOfUsers=numberOfUsers, numberOfLM=numberOfLM,
                           usersContainAdmin=usersContainAdmin, users_contain_test=users_contain_test,users_contain_companyName=users_contain_companyName,
                           users_contain_serviceAccount=users_contain_serviceAccount,
                            Not_Cracked=Not_Cracked,Cracked=get_total_passwords,
                             password_length=password_length,most_common_pass=most_common_pass)



'''
    Password Audit Page
    -------------------------------------------------------
'''

@app.route('/passwordAudit')
def passwordAudit():

    ''' Getting the password LIST from File Upload Class '''
    password_list                   = class_upload_files.get_password_list()

    get_total_passwords             = class_pass.total_passwords(password_list)
    unique_passwords                = class_pass.get_unique_passwords(password_list)

    password_length                 = class_pass.get_dict_password_length()
    most_common_pass                = class_pass.get_dict_most_common_pass()

    misc_pass                       = class_pass.get_passwords_misc(password_list)

    return render_template('passwordAudit.html', clientName=session['client_name'],total_passwords=get_total_passwords,
                           get_unique_passwords=0000,
                           password_length=password_length, most_common_pass=most_common_pass,
                           misc_pass=misc_pass,unique_passwords=unique_passwords)


# FILE UPLOAD PART
# ===========================================

#
# Route for HTML upload form page
#------------------------------------------

@app.route('/uploadFiles')
def uploadFile():
    return render_template('uploadFiles.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int('8889'), debug=True)
    #  app.debug = True
    #  app.run()
