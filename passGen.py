from fun import User,dis
import string 
from random import *
from math import *

print('welcome to 4RealPassGen! Enter 1 To login or 2 to register')
sell = input()
if sell == 1:
	print('enter username')
	username = input()
	print('enter password')
	passwrd = input()

if sell == 2:
	print('enter username')
	username = input()
	print('entter email')
	usermail = input()
	print('enter password')
	passwrd = input()
if sell != 1 and sell != 2 :
	print('INVALID INPUT')


print('enter name')
name = input()
print ('enter email')
email = input()
# pssword generator method
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(choice(characters)for x in range(8,16))
# print(password)
# print(len(password))

u1 = User(name, email, password)

dis(u1)