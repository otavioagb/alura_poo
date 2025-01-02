class Client:

    def __init__(self, identity=0, age=0, birth_year=0, email=''):
        self.identity = identity
        self.age = age
        self.birth_year = birth_year
        self.email = email


client = Client(12345678911, 52, 1970, '...')
print(vars(client))