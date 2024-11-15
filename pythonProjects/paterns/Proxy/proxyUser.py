from Proxy.User import User

class ProxyUser:
    def __init__(self, username):
        self.username = username

    def print_user(self):
        user = User(self.username)
        user.print_username()

