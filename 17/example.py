class User:
    
    def __init__(self, id, username):
        self.id = id
        self.username = username

user_1 = User(1, 'leo')

print(user_1.username, user_1.id)