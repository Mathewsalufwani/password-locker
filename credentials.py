class Credentials:

    '''
    The class that generates the credentials for the user
    '''

    credentials_list = []

    def __init__(self, service_provider, username, password):
        self.service_provider = service_provider
        self.username = username
        self.password = password

