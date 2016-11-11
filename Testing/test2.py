<<<<<<< HEAD
#!/usr/bin/env python

import sys
import argparse
from collections import defaultdict
import sys,re, os

user_hash = '/root/Projects/Domain-Password-Analyzer/Testing/user_hash.txt'
NTLM_password = '/root/Projects/Domain-Password-Analyzer/Testing/ntlm_pass.txt'

#user_hash contains most lines (users)
#hash_password is the short file, needs to be added to the user_hash file

Hash_dict_1 = dict();
Hash_dict_2 = dict();

with open(user_hash, 'r') as f:			# Username:Hash

	for i in f:
		data = i.strip().split(':');
		Hash_dict_1[data[0]] = data[1].strip();



with open(NTLM_password, 'r') as f:			# Username:Hash

	for i in f:
		data = i.strip().split(':');
		Hash_dict_2[data[0]] = data[1].strip();										#Hash:password


#combine:
print "below combine:\n"

user_hash_pass_list = []
#user_hash_pass = dict()
user_hash_pass_dict = ()

dict = {'key': ['v1']}

for username1,hash1 in Hash_dict_1.items():
	#print username1
	for hash2,password in Hash_dict_2.items():
		if hash1 == hash2:
			print username1+':'+hash1+':'+password
			user_hash_pass_list.append(username1+':'+hash1+':'+password)
			#user_hash_pass_dict[username1].append(username1+':'+hash1+':'+password)


print user_hash_pass_list

for i in user_hash_pass_list:
	a= i.strip().split(':')
	print a




'''
h1 = data[1][:16];
h2 = data[1][16:];
if h1 in Hash_dict:
	p1 = Hash_dict[h1];
else:
	p1 = "*******";
if h2 in Hash_dict:
	p2 = Hash_dict[h2];
else:
	p2 = "*******"

print data[0]+":"+data[1]+":"+p1+p2;

'''


'''
hash_dict = dict();
for i in args.plain_file:		#file containing hashes and plaintext passwords hash:plaintext
	s = i.split(':');
	hash_dict[s[0]] = s[1].strip();

for i in args.hash_file:			#file containing usernames and hashes username:hash
	s = i.strip().split(':');
	if (args.lm):
		h1 = s[1][:16];
		h2 = s[1][16:];
		if h1 in hash_dict:
			p1 = hash_dict[h1];
		else:
			p1 = "*******";
		if h2 in hash_dict:
			p2 = hash_dict[h2];
		else:
			p2 = "*******"

		print s[0]+":"+s[1]+":"+p1+p2;
	else:
		if s[1] in hash_dict:
			p = hash_dict[s[1]];
		else:
			p = "";
		print s[0]+":"+s[1]+":"+p;

'''
=======
from collections import Counter

local_file_NTDS = '/root/Projects/Dissector/Dissector-Nov-bootstrap/uploads/NTDS_Complete.txt'
local_file_passwords = '/root/Projects/Dissector/Dissector-Nov-bootstrap/uploads/PasswordsOnly.txt'
local_file_users_NTLM_Pass = '/root/Projects/Dissector/Dissector-Nov-bootstrap/uploads/users_NTLM_Pass.txt'

userLM =''
input =''
Total_users_equal_passwords = 0
myList = []

usernames =''
passwords =''
i =0

with open(local_file_passwords, 'r') as f:

	for i in f:
		myList.append(i)


counter =0
#print myList
newList = list(set(myList))
counter = Counter(newList)
a = len(newList)

print a
>>>>>>> b88926ce77d40736a1d28cc209a547845db10e4f

