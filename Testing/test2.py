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

