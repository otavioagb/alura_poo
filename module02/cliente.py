class Client:

    def __init__(self, id, age, birth_year, email):
        self.id = id
        self.age = age
        self.birth_year = birth_year
        self.email = email


client = Client(12795602152, 52, 1970, '...')
print(vars(client))