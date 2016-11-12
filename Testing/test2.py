
#!/usr/bin/env python

import sys
import argparse
from collections import defaultdict
from collections import Counter
import sys,re, os
passwords_only = '/root/Projects/Domain-Password-Analyzer/uploads/PasswordsOnly.txt'
user_hash = '/root/Projects/Domain-Password-Analyzer/Testing/user_hash.txt'
NTLM_password = '/root/Projects/Domain-Password-Analyzer/Testing/ntlm_pass.txt'

pass_dict = {}
pass_list = []

Hash_dict_1 = dict();
Hash_dict_2 = dict();

with open(passwords_only, 'r') as f:

	for i in f:
		data = i.split();
		pass_list.append(data[0])

print pass_list

a = Counter(pass_list).most_common(10)
print a
print a[1]
print a[1][0]

print '\n'



#print c.most_common(3)

print pass_dict.keys()

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

dict = {}
dict_1 = {}
all = ''

for username1,hash1 in Hash_dict_1.items():
	#print username1
	for hash2,password in Hash_dict_2.items():
		if hash1 == hash2:
			all =  username1+':'+hash1+':'+password
			user_hash_pass_list.append(username1+':'+hash1+':'+password)
			#user_hash_pass_dict[username1].append(username1+':'+hash1+':'+password)
			dict_1[username1] = all

#print dict_1.items()

for i in user_hash_pass_list:
	a= i.strip().split(':')
	#print a

	dict[a[0]] = a

#for key, value in dict.iteritems():
#	print value

#print dict.keys()
#print dict.items()




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



