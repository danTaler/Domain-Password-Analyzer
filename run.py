#!/usr/bin/env python
import os
from flask import Flask, request, redirect, url_for
from flask import render_template, session
from flask import send_from_directory
from werkzeug import secure_filename

from passwordAudit import CLASS_passwordAudit
from uploadedFiles import CLASS_upload_files_edit
from hackedAccount import class_haveibeenhacked

import os

'''
    General Configurations
    -----------------------------------------
'''
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt'])
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?AE'  #os.urandom(24)

''' global Classes '''
class_uploaded_files    = CLASS_upload_files_edit()
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

    MSG=MSG_2=''

    ''' Session for client name '''
    '''--------------------------------------------------'''
    if request.form['client_name']:
        clientName = request.form['client_name']
        session['client_name'] = clientName


    ''' Saving NTDS file  '''
    '''--------------------------------------------------'''
    if request.files['NTDS']:
        file_NTDS = request.files['NTDS']
        if file_NTDS and allowed_file(file_NTDS.filename):
            filename = secure_filename(file_NTDS.filename)

            file_NTDS.save(os.path.join(app.config['UPLOAD_FOLDER'],clientName+'_NTDS_'+filename))

            MSG_1 = 'OK'
            session['NTDS'] = True

            ''' Calling summary class functions once only !!! '''
            client_name = class_uploaded_files.show_client_name(session['client_name'])
            class_uploaded_files.get_files_from_upload_folder()

            ''' storing the ntds file into list '''
            class_uploaded_files.NTDS_into_Dic()



    ''' Saving password file '''
    '''--------------------------------------------------'''
    if request.files['CRACKED_PASSWORDS']:
        CRACKED_PASSWORDS = request.files['CRACKED_PASSWORDS']
        if CRACKED_PASSWORDS and allowed_file(CRACKED_PASSWORDS.filename):
            filename = secure_filename(CRACKED_PASSWORDS.filename)

            CRACKED_PASSWORDS.save(os.path.join(app.config['UPLOAD_FOLDER'], clientName+'_passwords_'+filename))

            MSG_2 = 'OK'

            session['passwords'] = True

            '''== password class =='''
            client_name = class_pass.show_client_name(session['client_name'])
            class_pass.load_pass_file()
            class_pass.PASSWORDS_into_list()

            ''' Calling password class functions once only !!! '''
            class_pass.password_length()
            class_pass.most_common_password()


    return render_template('uploadFiles.html', NTDS=MSG_1, CRACKED_PASSWORDS=MSG_2 )


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


            numberOfUsers = class_uploaded_files.number_of_username_NTDS()

            numberOfLM = class_uploaded_files.number_of_LMs()

            usersContainAdmin = class_uploaded_files.users_contain_admin()
            users_contain_test = class_uploaded_files.users_contain_test()
            users_contain_companyName = class_uploaded_files.users_contain_companyName()
            users_contain_serviceAccount = class_uploaded_files.users_contain_serviceAccount()


            ''' == Class password functions == '''
            password_length = class_pass.get_dict_password_length()

            get_total_passwords = class_pass.total_passwords()


            Not_Cracked = (numberOfUsers - get_total_passwords)

            most_common_pass = class_pass.get_dict_most_common_pass()


            ''' == class_haveibeenhacked == '''

            #pwn = class_haveibeenhacked()
            #pwn.haveibeenhacked()

            return render_template('Summary.html',client_name=client_name, numberOfUsers=numberOfUsers, numberOfLM=numberOfLM,
                           usersContainAdmin=usersContainAdmin, users_contain_test=users_contain_test,users_contain_companyName=users_contain_companyName,
                           users_contain_serviceAccount=users_contain_serviceAccount,
                            Not_Cracked=Not_Cracked,Cracked=get_total_passwords,
                            password_length=password_length, most_common_pass=most_common_pass)






'''
    Password Audit Page
    -------------------------------------------------------
'''

@app.route('/passwordAudit')
def passwordAudit():

    #client_name = class_pass.show_client_name(session['client_name'])

    #class_pass.load_pass_file()
    #class_pass.PASSWORDS_into_list()

    get_total_passwords = class_pass.total_passwords()

    #get_unique_passwords = class_pass.get_unique_passwords()

    password_length = class_pass.get_dict_password_length()
    most_common_pass = class_pass.get_dict_most_common_pass()

    misc_pass = class_pass.get_passwords_misc()

    return render_template('passwordAudit.html', clientName=session['client_name'],total_passwords=get_total_passwords,
                           get_unique_passwords=0000,
                           password_length=password_length, most_common_pass=most_common_pass,
                           misc_pass=misc_pass)


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
