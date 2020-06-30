import pyperclip
import random
from user import User
from credentials import Credentials
import login
from termcolor import colored, cprint

def create_user(service_provider, username, password):
    '''
    Create User
    '''
    new_user = User( username, password)
    return new_user

def create_credentials(service_provider, username, password):
    '''
    Create credentials
    '''
    new_credentials = Credentials(service_provider, username, password)
    return new_credentials

def save_user(user):
    '''
    save user
    '''
    user.save_user()

def save_credentials(credentials):
    '''
    save user credentials
    '''
    credentials.save_credentials()

def delete_user(user):
    '''
    delete saved user
    '''
    user.delete_user()

def delete_credentials(credentials):
    '''
    delete saved credentials
    '''
    credentials.delete_credentials()

def display_user():
    '''
    Method to display saved user
    '''
    return User.display_user()

def find_user_by_username(cls,username):
        '''
        Method that takes in a service provider and returns a user that matches that service provider.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user    