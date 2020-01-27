#! /usr/bin/env python3 
from user import User, user_details
import string 
from random import *
from math import *

def add_used(user_name, password):
	'''
	Function to add user account to the system
	'''
	newUser = User(user_name, password)
	return newUser

def user_acc
	'''
	A function to save the user account after user enters detsils
	'''
	User.user_acc(user)

def verify (name, password)
	'''
	This is a function that verifies the existance of a user on login 
	'''
	user_check = user_details.check_user(name,password)
	return user_check
def password_gen():
	'''
	Function that generates passwords automatically
	'''
	pass_gen = user_details.password_gen()
	return pass_gen
def create_user(uname, acc_name, password):
	'''
	function to create new user object for user details
	'''
	 user1 = user_details(uname, acc_name, password)
	 return user1
	def save_user_details(user_details):
		'''
		Function for saving a newly created/added user
		'''
		return user_details.save_user_details(user_details)



print(' ')
print('welcome to 4RealPassGen! Enter 1 To login or 2 to register')
print(' ')
sell = input()
if sell == 1:
	username = input('enter username').strip
	passwrd = input('enter password').strip

if sell == 2:
	print('enter username')
	username = input()
	print('entter email')
	usermail = input()
	print('enter password')
	passwrd = input()
if sell != 1 and sell != 2 :
	print('INVALID INPUT')




characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(choice(characters)for x in range(8,16))
# print(password)
# print(len(password))

u1 = User(username, email, password)

dis(u1)