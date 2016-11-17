import sys,re, os
from collections import defaultdict

from urllib2 import Request, urlopen, URLError
import urllib2
from random import randint
from time import sleep

''''
    This class:
        takes the files (uploads) and store them for next processing.
        store the files in lists and dictionary:
            1. NTDS into lists
            2. Passwords Only file into lists
            3. Hash_Password file

'''

class CLASS_upload_files_edit():

    ''' Input:  files: NTDS, Password-Only File, Hash-Password File.
        ------------------------------------------------------
    '''


    list_NTDS_file      = []    # List =>  [['user1', '500', 'aad3b43..', '3dd97e0fd...'], ['use2', '502', 'aad3...', '2b7...'],...
    list_passwords      = []
    list_passwords_updated = []
    dict_passwords      = {}
    list_Hash_pass      = []            #   hash:hash
    list_Hash_pass_PasswordOnly = []    #   passwordsOnly
    list_user_hash_pass = []            #   User:Hash:Password

    Client_Name      = ''
    file_name_NTDS   = ''


    '''
        Getting List Functions:
    '''
    def show_client_name(self,client_name):

        self.Client_Name = client_name
        return self.Client_Name


    def get_ntds_list(self):
        return self.list_NTDS_file


    def make_password_list(self):
        for i in self.list_passwords:                   #the list is: ['xx].['xx'],['xx']  List of lists
            self.list_passwords_updated.append(i[0])    #making the list: ['pass', 'pass1', 'pass2', 'pass3']


    def get_password_list_updated(self):
        return self.list_passwords_updated      #returning the list: ['pass', 'pass1', 'pass2', 'pass3']

    def get_password_dict(self):
        return self.dict_passwords

    def make_passwords_of_hash_pass_file(self):
        for x in self.list_Hash_pass:

            self.list_Hash_pass_PasswordOnly.append(x[1])

    def get_passwords_of_hash_pass_file_PASSWORDSonly(self):
        return self.list_Hash_pass_PasswordOnly


    def get_user_hash_pass(self):               # Get ['USER:HASH:PASSWORD', 'USER:HASH:PASSWORD']
        return self.list_user_hash_pass



    ''' Saving NTDS File into list '''

    def NTDS_into_List(self):

        uploads_directory = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'

        for file_name in os.listdir(uploads_directory):

            if file_name.startswith(self.Client_Name+'_NTDS_') and file_name.endswith(".txt"):
                self.file_name_NTDS = file_name


        NTDS_file = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'+self.file_name_NTDS

        with open(NTDS_file, 'r') as f:

            for i in f:
                data = i.strip().split(':');
                if data[0] != '':
                    self.list_NTDS_file.append(data) # Into List




    ''' Saving Password Only file into list '''

    def PASSWORDS_into_list(self):

		uploads_directory = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'

		for file_name in os.listdir(uploads_directory):

			if file_name.startswith(self.Client_Name+'_passwords_') and file_name.endswith(".txt"):
				file_name_passwords = file_name

		Password_file = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'+file_name_passwords

		with open(Password_file,'r') as f:

			for i in f:
				data = i.strip().split(':')

				if data[0] != '':
					self.list_passwords.append(data)
					self.dict_passwords[i] = data



    ''' Saving Hash_Pasword file into list '''
    def Hash_Pass_into_list(self):

        Hash_Pass_file = ''
        NTDS_file = ''

        uploads_directory = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'
        for file_name in os.listdir(uploads_directory):

            if file_name.startswith(self.Client_Name+'_hash_pass_') and file_name.endswith(".txt"):
                 Hash_Pass_file=file_name

        Hash_dict_1 = dict();

        file_open = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'+''+Hash_Pass_file

        with open(file_open, 'r') as f:

            for i in f:
                #print i
                data = i.strip().split(':');
                #print data
                #Hash_dict_1[data[0]] = data[1].strip();
                self.list_Hash_pass.append(data)


		#for key,value in Hash_dict_1.iteritems():
		#	print key, value


		#print Hash_dict_1.items()



    def merge_ntds_with_hashPass_file(self):


        ''' Merging the lists '''
        for user_hash in self.list_NTDS_file:
            #print user_hash[0],user_hash[3], 'NTLM_HASH'             #username:NTLM

            for hash_pass in self.list_Hash_pass:
                #print hash_pass[0], hash_pass[1], 'hash_pass'
                if user_hash[3] == hash_pass[0]:
                    #all +=  user_hash[0]+':'+user_hash[3]+':'+hash_pass[1]+ '\n'
                    self.list_user_hash_pass.append(user_hash[0]+':'+user_hash[3]+':'+hash_pass[1])
                    #print 'HERE'


        #print self.list_user_hash_pass










    '''
        simple user names exists: user, archive, backup, abc, events, security, hr,
        payroll, finance, student, tablet, feedback,servicedesk, ithelpdesk, support, training, temp,infodesk,employment, internet,info
    '''



    '''
        Overall Risk based on number of LMS, week passwords...
    '''


    '''
        Hacked Account:
            https://haveibeenpwned.com/api/v2/breachedaccount/<username>@company.com?truncateResponse=true

        security issue:
            cannot test all users:

        should test only users with week passwords?
        should ask the client to confirm before uploading.

        should ask the user to input which user to check!
    '''


    def get_hacked_user(self,username):


        req = urllib2.Request('https://haveibeenpwned.com/api/v2/breachedaccount/'+username+'@'+self.Client_Name+'?truncateResponse=true')
        req.add_header('Accept', 'application/vnd.haveibeenpwned.v2+json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>')

        try:
            resp = urllib2.urlopen(req)
            content = resp.read()

            print content
          #  sleep(randint(5,20))
        except URLError, e:
            print 'No kittez. Got an error code:', e





