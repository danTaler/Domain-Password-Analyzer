import sys,re, os
from collections import defaultdict

from urllib2 import Request, urlopen, URLError
import urllib2
from random import randint
from time import sleep



class CLASS_summary():

    ''' Showing results for the Summary Page.
        Some password results are from the Password Class not shown here.
        ------------------------------------------------------
    '''

    Client_Name      = ''



    '''
        Client name passed by session
    '''
    def show_client_name(self,client_name):

        self.Client_Name = client_name
        return self.Client_Name


    def number_of_username_NTDS(self,ntds_list):

        num_of_users = len(ntds_list)

        return num_of_users


    def number_of_LMs(self,ntds_list):

        count = 0

        for LM in ntds_list:
            if (LM[2] != 'aad3b435b51404eeaad3b435b51404ee'):
                count +=1
        return count


    def users_contain_admin(self,ntds_list):

        count = 0

        for admin in ntds_list:

            if (re.search(r'admin',admin[0], re.IGNORECASE)):
               # print admin[0]
                count +=1
        return count


    def users_contain_test(self,ntds_list):

        count = 0

        for test in ntds_list:

            if (re.search(r'test',test[0], re.IGNORECASE)):
               # print test[0]
                count +=1
        return count


    def users_contain_companyName(self,ntds_list,client_name):

        count = 0
        company_name = client_name

        for companyName in ntds_list:

            if (re.search(company_name,companyName[0], re.IGNORECASE)):

                count +=1
        return count


    def users_contain_serviceAccount(self,ntds_list):

        count = 0

        for serviceAccount in ntds_list:

            if (re.search(r'\$',serviceAccount[0], re.IGNORECASE)):

                count +=1

        return count


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