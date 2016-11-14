from collections import Counter
from collections import defaultdict
import re, os



class CLASS_passwordAudit():

	Client_Name 		= ''

	dict_length = {}
	dict_most_common_pass = {}


	def show_client_name(self,client_name):

		self.Client_Name = client_name
		return self.Client_Name


	def get_dict_password_length(self):
		return self.dict_length





	def total_passwords(self,password_list):

		Total_passwords = len(password_list)
		#print Total_passwords
		return Total_passwords



	'''
			Unique passwords
	'''
	def get_unique_passwords(self,password_list):

		new_list = []

		for i in password_list:
			new_list.append(i[0])

		myset = set(new_list)

		return len(myset)




	def password_length(self,list_passwords):

		zero=one=two=three=four=five=six=seven=eight=nine=ten=eleven=twelve=thirsteen=fourteen=fifteen=zero_to_seven_chars = 0
		over_eight_chars =0

		dict = {'six': 0, 'one': 0, 'two':0, 'three':0, 'four':0, 'five':0, 'six':0}

		for password in list_passwords:

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

		self.dict_length['zero'] 	= zero
		self.dict_length['one'] 	= one
		self.dict_length['two'] 	= two
		self.dict_length['three'] 	= three
		self.dict_length['four'] 	= four
		self.dict_length['five'] 	= five
		self.dict_length['six'] 	= six
		self.dict_length['seven']	= seven
		self.dict_length['eight'] 	= eight
		self.dict_length['nine'] 	= nine
		self.dict_length['ten'] 	= ten
		self.dict_length['eleven'] 	= eleven
		self.dict_length['twelve'] 	= twelve
		self.dict_length['thirsteen'] 	= thirsteen
		self.dict_length['fourteen'] 	= fourteen
		self.dict_length['fifteen'] 	= fifteen

		self.dict_length['over_eight_chars'] 	= over_eight_chars

		#zero_to_seven_chars = (zero + one + two + three + four + five + six + seven)
		self.dict_length['zero_to_seven_chars'] = zero_to_seven_chars


		# Percentage by passwords or total users :
		# ---
		Tota_Accounts = self.total_passwords(list_passwords)

		self.dict_length['zero_percent'] = "{0:.2f}%".format((zero / float(Tota_Accounts)) * 100)
		self.dict_length['one_percent'] = "{0:.2f}%".format((one / float(Tota_Accounts)) * 100)
		self.dict_length['two_percent'] = "{0:.2f}%".format((two / float(Tota_Accounts)) * 100)
		self.dict_length['three_percent'] = "{0:.2f}%".format((three / float(Tota_Accounts)) * 100)
		self.dict_length['four_percent'] = "{0:.2f}%".format((four / float(Tota_Accounts)) * 100)
		self.dict_length['five_percent'] = "{0:.2f}%".format((five / float(Tota_Accounts)) * 100)
		self.dict_length['six_percent'] = "{0:.2f}%".format((six / float(Tota_Accounts)) * 100)
		self.dict_length['seven_percent'] = "{0:.2f}%".format((seven / float(Tota_Accounts)) * 100)
		self.dict_length['eight_percent'] = "{0:.2f}%".format((eight / float(Tota_Accounts)) * 100)
		self.dict_length['nine_percent'] = "{0:.2f}%".format((nine / float(Tota_Accounts)) * 100)
		self.dict_length['ten_percent'] = "{0:.2f}%".format((ten / float(Tota_Accounts)) * 100)
		self.dict_length['eleven_percent'] = "{0:.2f}%".format((eleven / float(Tota_Accounts)) * 100)
		self.dict_length['twelve_percent'] = "{0:.2f}%".format((twelve / float(Tota_Accounts)) * 100)
		self.dict_length['thirsteen_percent'] = "{0:.2f}%".format((thirsteen / float(Tota_Accounts)) * 100)
		self.dict_length['fourteen_percent'] = "{0:.2f}%".format((fourteen / float(Tota_Accounts)) * 100)
		self.dict_length['fifteen_percent'] = "{0:.2f}%".format((fifteen / float(Tota_Accounts)) * 100)



	def get_dict_most_common_pass(self):

		return self.dict_most_common_pass

#  1. Need to find most commons NTLM hashes   (Hashcat will only crack unique values)
# 		Even the hashcat.pot file will display unique values

	def most_common_password(self,password_list):

		new_list = []

		for i in password_list:
			new_list.append(i[0])

		common_password = Counter(new_list).most_common(10)


		self.dict_most_common_pass['most_common_pass'] = common_password[0][0]
		self.dict_most_common_pass['most_common_pass_count'] = common_password[0][1]

		self.dict_most_common_pass['2nd most common'] = common_password[1][0]
		self.dict_most_common_pass['2nd most common count'] = common_password[1][1]

		self.dict_most_common_pass['3rd most common'] = common_password[2][0]
		self.dict_most_common_pass['3rd most common count'] = common_password[2][1]

		self.dict_most_common_pass['4th most common'] = common_password[3][0]
		self.dict_most_common_pass['4th most common count'] = common_password[3][1]

		self.dict_most_common_pass['5th most common'] = common_password[4][0]
		self.dict_most_common_pass['5th most common count'] = common_password[4][1]

		self.dict_most_common_pass['6th most common'] = common_password[5][0]
		self.dict_most_common_pass['6th most common count'] = common_password[5][1]

		self.dict_most_common_pass['7th most common'] = common_password[6][0]
		self.dict_most_common_pass['7th most common count'] = common_password[6][1]

		self.dict_most_common_pass['8th most common'] = common_password[7][0]
		self.dict_most_common_pass['8th most common count'] = common_password[7][1]

		self.dict_most_common_pass['9th most common'] = common_password[8][0]
		self.dict_most_common_pass['9th most common count'] = common_password[8][1]

		self.dict_most_common_pass['10th most common'] = common_password[9][0]
		self.dict_most_common_pass['10th most common count'] = common_password[9][1]



## -- Misc Passwords Table
##
#  1. Numbers only
#  2. Lower Case Only
#
	def get_passwords_misc(self,password_list):

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

		for password in password_list:

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