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