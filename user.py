class User:
    

    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for our objects.
        '''
        
        self.username = username
        self.password = password

    user_list = []  # Empty user list    
    # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self) 

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)