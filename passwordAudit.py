from collections import Counter
from collections import defaultdict
import re, os



class CLASS_passwordAudit():

	Client_Name 		= ''
	file_name_passwords = ''
	list_passwords 		= []

	dict = {}
	dict_most_common_pass = {}

	def show_client_name(self,client_name):

		self.Client_Name = client_name
		return self.Client_Name


	def get_dict_password_length(self):
		return self.dict


	def load_pass_file(this):

		uploads_directory = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'

		for file_name in os.listdir(uploads_directory):

			if file_name.startswith(this.Client_Name+'_passwords_') and file_name.endswith(".txt"):
				this.file_name_passwords = file_name



	def PASSWORDS_into_list(self):

		Password_file = os.path.dirname(os.path.realpath(__file__)) + '/uploads/'+self.file_name_passwords

		''' Check if file exist already '''

		with open(Password_file,'r') as f:

			for i in f:
				data = i.strip().split(':')

				if data[0] != '':
					self.list_passwords.append(data)


	def total_passwords(self):

		Total_passwords = len(self.list_passwords)
		#print Total_passwords
		return Total_passwords


	'''
			To DO:  Unique pass
	'''
	def get_unique_passwords(self):
		counter = 0
		newList = []
		output = set()

		for x in self.list_passwords:
			print x
			#output.add(x)
		#print output
		mylist = list(set(self.list_passwords))

		return counter



	def password_length(self):

		zero=one=two=three=four=five=six=seven=eight=nine=ten=eleven=twelve=thirsteen=fourteen=fifteen=zero_to_seven_chars = 0
		over_eight_chars =0

		dict = {'six': 0, 'one': 0, 'two':0, 'three':0, 'four':0, 'five':0, 'six':0}

		for password in self.list_passwords:

				#--length---
				if len(password[0]) == 0:
					zero +=1

				if len(password[0]) == 1:
					one +=1

				if len(password[0]) == 2:
					two +=1

				if len(password[0]) == 3:
					three +=1

				if len(password[0]) == 4:
					four +=1

				if len(password[0]) == 5:
					five +=1

				if len(password[0]) == 6:
					six +=1

				if len(password[0]) == 7:
					seven +=1

				if len(password[0]) == 8:
					eight +=1

				if len(password[0]) == 9:
					nine +=1

				if len(password[0]) == 10:
					ten +=1

				if len(password[0]) == 11:
					eleven +=1

				if len(password[0]) == 12:
					twelve +=1

				if len(password[0]) == 13:
					thirsteen +=1

				if len(password[0]) == 14:
					fourteen +=1

				if len(password[0]) == 15:
					fifteen +=1

				if len(password[0]) > 8:
					over_eight_chars +=1

				if len(password[0]) < 8:
					zero_to_seven_chars +=1

		self.dict['zero'] 	= zero
		self.dict['one'] 	= one
		self.dict['two'] 	= two
		self.dict['three'] 	= three
		self.dict['four'] 	= four
		self.dict['five'] 	= five
		self.dict['six'] 	= six
		self.dict['seven']	= seven
		self.dict['eight'] 	= eight
		self.dict['nine'] 	= nine
		self.dict['ten'] 	= ten
		self.dict['eleven'] 	= eleven
		self.dict['twelve'] 	= twelve
		self.dict['thirsteen'] 	= thirsteen
		self.dict['fourteen'] 	= fourteen
		self.dict['fifteen'] 	= fifteen

		self.dict['over_eight_chars'] 	= over_eight_chars

		#zero_to_seven_chars = (zero + one + two + three + four + five + six + seven)
		self.dict['zero_to_seven_chars'] = zero_to_seven_chars


		# Percentage by passwords or total users :
		# ---
		Tota_Accounts = self.total_passwords()

		self.dict['zero_percent'] = "{0:.2f}%".format((zero / float(Tota_Accounts)) * 100)
		self.dict['one_percent'] = "{0:.2f}%".format((one / float(Tota_Accounts)) * 100)
		self.dict['two_percent'] = "{0:.2f}%".format((two / float(Tota_Accounts)) * 100)
		self.dict['three_percent'] = "{0:.2f}%".format((three / float(Tota_Accounts)) * 100)
		self.dict['four_percent'] = "{0:.2f}%".format((four / float(Tota_Accounts)) * 100)
		self.dict['five_percent'] = "{0:.2f}%".format((five / float(Tota_Accounts)) * 100)
		self.dict['six_percent'] = "{0:.2f}%".format((six / float(Tota_Accounts)) * 100)
		self.dict['seven_percent'] = "{0:.2f}%".format((seven / float(Tota_Accounts)) * 100)
		self.dict['eight_percent'] = "{0:.2f}%".format((eight / float(Tota_Accounts)) * 100)
		self.dict['nine_percent'] = "{0:.2f}%".format((nine / float(Tota_Accounts)) * 100)
		self.dict['ten_percent'] = "{0:.2f}%".format((ten / float(Tota_Accounts)) * 100)
		self.dict['eleven_percent'] = "{0:.2f}%".format((eleven / float(Tota_Accounts)) * 100)
		self.dict['twelve_percent'] = "{0:.2f}%".format((twelve / float(Tota_Accounts)) * 100)
		self.dict['thirsteen_percent'] = "{0:.2f}%".format((thirsteen / float(Tota_Accounts)) * 100)
		self.dict['fourteen_percent'] = "{0:.2f}%".format((fourteen / float(Tota_Accounts)) * 100)
		self.dict['fifteen_percent'] = "{0:.2f}%".format((fifteen / float(Tota_Accounts)) * 100)

		print 'making dictionary'

	def get_dict_most_common_pass(self):

		return self.dict_most_common_pass

#  1. Need to find most commons NTLM hashes   (Hashcat will only crack unique values)
# 		Even the hashcat.pot file will display unique values

	def most_common_password(self):

		dict = {}
		temp_list_passwords 		= []
		temp_2_list_passwords 		= []

		most_common_pass = max((self.list_passwords), key=self.list_passwords.count)

		self.dict_most_common_pass['most_common_pass'] = most_common_pass[0]
		self.dict_most_common_pass['most_common_pass_count'] = self.list_passwords.count(most_common_pass)

		for i in self.list_passwords:

			if most_common_pass[0] != i[0]:
				#print i[0]
				temp_list_passwords.append(i[0])       # list without most common!


		second_most_common_pass = max((temp_list_passwords), key=temp_list_passwords.count)

		self.dict_most_common_pass['2nd most common'] = second_most_common_pass
		self.dict_most_common_pass['2nd most common count'] = temp_list_passwords.count(second_most_common_pass)


		for i in temp_list_passwords:

			if second_most_common_pass[0] != i[0]:

				temp_2_list_passwords.append(i)

		third_most_common_pass = max((temp_2_list_passwords), key=temp_2_list_passwords.count)

		self.dict_most_common_pass['3rd most common'] = third_most_common_pass
		self.dict_most_common_pass['3rd most common count'] = temp_2_list_passwords.count(third_most_common_pass)



## -- Misc Passwords Table
##
#  1. Numbers only
#  2. Lower Case Only
#
	def get_passwords_misc(self):

		pattern_numbers_only    	= re.compile("^[0-9]+$")
		pattern_lowercase_only  	= re.compile("^[a-z]+$")
		pattern_uppercase_only  	= re.compile("^[A-Z]+$")
		pattern_special_char_only   = re.compile("^[\W]+$")

		pattern_FIRST_CAP_LAST_NUM_RE = re.compile("^[A-Z].*[0-9]$")
		pattern_FIRST_CAP_LAST_SYMBOL_RE = re.compile("^[A-Z].*[\W]$")

		pattern_SINGLES_ON_END_RE = re.compile("[^0-9]+([0-9]{1})$")   # Ending with 1 numbers
		pattern_DOUBLES_ON_END_RE = re.compile("[^0-9]+([0-9]{2})$")   # Ending with 2 numbers
		pattern_TRIPLES_ON_END_RE = re.compile("[^0-9]+([0-9]{3})$")   # Ending with 3 numbers

		pattern_lowercase_numbers = re.compile("^[a-z0-9]+$")
		pattern_uppercase_numbers = re.compile("^[A-Z0-9]+$")

		numbers_only     = 0
		lower_case_only  = 0
		upper_case_only   = 0
		special_char_only     = 0

		FIRST_CAP_LAST_NUM_RE = 0
		FIRST_CAP_LAST_SYMBOL_RE = 0

		over_eight_chars = 0

		SINGLES_ON_END_RE = 0
		DOUBLES_ON_END_RE = 0
		TRIPLES_ON_END_RE = 0

		lowercase_numbers = 0
		uppercase_numbers = 0

		dict = {'numbers_only':[],'lowercase_only':[],'upper_case_only':[], 'special_char_only':[]}

		for password in self.list_passwords:

				if re.search(pattern_numbers_only,password[0]):
					numbers_only = numbers_only + 1

				if re.search(pattern_lowercase_only,password[0]):
					lower_case_only = lower_case_only + 1

				if re.search(pattern_uppercase_only,password[0]):
					upper_case_only = upper_case_only + 1


				if re.search(pattern_FIRST_CAP_LAST_NUM_RE,password[0]):
					FIRST_CAP_LAST_NUM_RE = FIRST_CAP_LAST_NUM_RE + 1

				if re.search(pattern_FIRST_CAP_LAST_SYMBOL_RE,password[0]):
					FIRST_CAP_LAST_SYMBOL_RE = FIRST_CAP_LAST_SYMBOL_RE + 1

				if re.search(pattern_special_char_only,password[0]):
					special_char_only = special_char_only + 1
#				if re.search(over_eight_chars,password):
#					over_eight_chars = over_eight_chars + 1


				if re.search(pattern_SINGLES_ON_END_RE,password[0]):
					SINGLES_ON_END_RE = SINGLES_ON_END_RE + 1

				if re.search(pattern_DOUBLES_ON_END_RE,password[0]):
					DOUBLES_ON_END_RE = DOUBLES_ON_END_RE + 1

				if re.search(pattern_TRIPLES_ON_END_RE,password[0]):
					TRIPLES_ON_END_RE = TRIPLES_ON_END_RE + 1

				if re.search(pattern_lowercase_numbers,password[0]):
					lowercase_numbers = lowercase_numbers + 1

				if re.search(pattern_uppercase_numbers,password[0]):
					uppercase_numbers = uppercase_numbers + 1

		dict['numbers_only'] = numbers_only
		dict['lower_case_only'] = lower_case_only
		dict['upper_case_only'] = upper_case_only
		dict['special_char_only'] = special_char_only

		dict['FIRST_CAP_LAST_NUM_RE'] = FIRST_CAP_LAST_NUM_RE
		dict['FIRST_CAP_LAST_SYMBOL_RE'] = FIRST_CAP_LAST_SYMBOL_RE

		dict['SINGLES_ON_END_RE'] = SINGLES_ON_END_RE  # Ending with 1 numbers
		dict['DOUBLES_ON_END_RE'] = DOUBLES_ON_END_RE	# Ending with 2 numbers
		dict['TRIPLES_ON_END_RE'] = TRIPLES_ON_END_RE	# Ending with 3 numbers

		dict['lowercase_numbers'] = lowercase_numbers
		dict['uppercase_numbers'] = uppercase_numbers

		return dict


'''



	def get_most_common_single_password(self,myDictionary):
	#	print myDictionary['count']
	#	print myDictionary.keys()

		for b in myDictionary.items():
			print  b[1]
			#print b['pass']
		#maximum = max(myList['count'])

		return 333



		Tota_Accounts = self.get_total_accounts()

		list1 = []
		for line in f:
		 list1.append(line)

		counter = Counter(list1)

		d = {'pass':[],'count':[],'percent':[]}
		#counter = Counter(list1)

		for word, count in counter.most_common(10):

			a = "{0:.2f}%".format((count / float(Tota_Accounts)) * 100)
			d['percent'].append(a)
			d['pass'].append(word)
			d['count'].append(count)

		return d



	def get_guessable_passwords(self):
		num_lines = sum(1 for line in open(FILE_GUESSABLE_PASSWORDS))
		return num_lines


	def users_equal_passwords(self):
		Total_users_equal_passwords = 0

		with open(FILE_USERS_NTLM_PASSWORDS, 'r') as f:

			for i in f:

				input = i.rstrip().split(':')
				#print input[0]
				if (input[0] == input[2]):
					Total_users_equal_passwords +=1

		return Total_users_equal_passwords

	'''