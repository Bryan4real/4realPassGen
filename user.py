import string 

global proifle

class User:
	'''
	Class to create and save user accounts with details
	'''
	profile[]
	def __init__(self, name, password):
		'''
		constructor/method to define properties for each user object
		'''

		self.name = name
		# self.email = email
		self.password = password

	def user_acc(self):
	'''
	Function to save a new accout that is created by the user
	'''
	User.profile.append(self)

class user_details:
	'''
	class to create and save user account details and generate passwords 
	'''
	details_list = []
	user_details_list = []
	@classmethod
	def check_user(cls,name,password):
		'''
		method to check if the info entered matches ones in the profile 
		'''
		current_user = ''
		for user in User.profile:
			if  user.name ==  name and user.password == password:
				current_user = user.name
		return current_user
	def __init__(self,uname, acc_name, password):
		'''
		Method that defines properties of each user objeect
		'''
		self.uname = uname
		self.acc_name = acc_name
		self.password = password
	def save_user_details(self):
		'''
		Function to save new user object
		'''
		user_details.details_list.append(self)

	def password_gen():
		'''
		Function to generate an 8 character password for user
		'''
		characters = string.ascii_letters + string.digits + string.punctuation
		pass_gen = "".join(choice(characters)for x in range(8,16))
		return pass_gen
	@classmethod
	def display_user_details(cls,uname):
		'''
		class method to display user_details saved
		'''
		user_details_list = []
		for user_details in cls.details_list:
			if user_details.uname == uname:
				user_details_list.append(user_details)
		return user_details_list



# def dis(self):
# 	print('your details ' + self.name + self.email + self.password)

			
# u1 = User('Bryan', 'mwiruki@outlook.com', 'password')

# dis(u1)
