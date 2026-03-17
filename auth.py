class Authentification:
    def __init__(self):
        self.users = {}
    
    def login(self, username, password):
        return self.users.get(username) == password
