from fun import User,dis
import string 
from random import *
from math import *

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(choice(characters)for x in range(8,16))
# print(password)
# print(len(password))

print('enter name')
name = input()
print ('enter email')
email = input()

u1 = User(name, email, password)

dis(u1)