import unittest
import pyperclip
from user_credentials import User, Credential


class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Bryan,'Q1%c{/}')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'Bryan')
		self.assertEqual(self.new_user.password,'Q1%c{/}')

    def test_user_acc(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.user_acc()
		self.assertEqual(len(User.profile),1)

    class Test_user_details(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''