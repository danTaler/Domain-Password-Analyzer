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

    # List =>  [['user1', '500', 'aad3b43..', '3dd97e0fd...'], ['use2', '502', 'aad3...', '2b7...'],...
    list_NTDS_file      = []
    list_passwords      = []
    dict_passwords      = {}

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


    def get_password_list(self):
        return self.list_passwords


    def get_password_dict(self):
        return self.dict_passwords



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




    def merge_ntds_with_hashPass_file(self):

		Hash_Pass_file = ''
		NTDS_file = ''

		uploads_directory = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'
		for file_name in os.listdir(uploads_directory):

			if file_name.startswith(self.Client_Name+'_hash_pass_') and file_name.endswith(".txt"):
				Hash_Pass_file=file_name

			if file_name.startswith(self.Client_Name+'_NTDS_') and file_name.endswith(".txt"):
				NTDS_file = file_name

		Hash_dict_1 = dict();

		file_open = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'+''+Hash_Pass_file

		with open(file_open, 'r') as f:			# Hash:pass

			for i in f:
				data = i.strip().split(':');
				Hash_dict_1[data[0]] = data[1].strip();

		for key,value in Hash_dict_1.iteritems():
			print key, value


		print Hash_dict_1.items()


		Hash_dict_2 = dict();

		''' NTDS File, can just load it from NTDS class in the future'''

		file_open = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'+''+NTDS_file
		with open(file_open, 'r') as f:			# Username:Hash

			for i in f:
				data = i.strip().split(':');
				Hash_dict_2[data[0]] = data[3].strip();


		print Hash_dict_2.items()

		user_hash_pass_list = []
		dict_1 = {}

		''' Merging the dictionaries '''
		for username1,hash1 in Hash_dict_1.items():
			print username1, hash1
			for hash2,password in Hash_dict_2.items():
				#print hash2, password
				if hash1 == hash2:

					all =  username1+':'+hash1+':'+password
					user_hash_pass_list.append(username1+':'+hash1+':'+password)
					#user_hash_pass_dict[username1].append(username1+':'+hash1+':'+password)
					dict_1[username1] = all

		print dict_1.items()

		for username1,hash1 in Hash_dict_1.items():
			print username1, hash1



    ''' OLD -------- '''







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


    # Stich all passwords to USERS:HASHES

    # Create a dictionary file of:
    #   username: (username,ID, LM, NTLM, password)
    # and
    #  username: (username,ID, LM, NTLM, < > )

    def combine_USER_HASH_PASS(self,NTDS,file_GUESSABLE):

        dict_NTDS                = dict()
        dict_guessable_passwords = dict()
        dict_masks_passwords     = dict()

        file_path = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'
        NTDS = NTDS
        file_GUESSABLE = file_GUESSABLE


        with open(file_path+'NTDS.txt', 'r') as f:

            for i in f:
                data = i.strip().split(':');

                if data[0] != '':
                    dict_NTDS[data[0]] = data[3],data[1]
  #                  dict_NTDS[data[1]] = data[1]

        #print dict_NTDS.items()
        #print dict_NTDS.keys()

        with open(file_path+'rockyou.txt','r') as f:
            for j in f:
                data = j.strip().split(':')
                dict_guessable_passwords[data[0]] = data[1]


        dict_USER_HASH_PASS = {}

        for hashValue_passFile, password in dict_guessable_passwords.iteritems():

            for username, hashValue_NTDS in dict_NTDS.iteritems():

                if hashValue_NTDS == hashValue_passFile:
                    #print 'found ' + username, hashValue_NTDS, password

                    dict_USER_HASH_PASS[username] = username,hashValue_NTDS, password

      #  print dict_USER_HASH_PASS

        return dict_USER_HASH_PASS