import unittest
import random
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James", "0875345") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        #self.assertEqual(self.new_user.service_provider,"Instagram")
        self.assertEqual(self.new_user.username,"James")
        self.assertEqual(self.new_user.password, "0875345")

    def test_save_user(self):
        '''
        save user method
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        '''
        Method that does the clean up after each test run
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User( "user", "1233")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

if __name__ == '__main__':
    unittest.main()