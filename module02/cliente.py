# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie um objeto desta classe e atribua valores aos seus atributos através de um método construtor.

class Client:

    def __init__(self, id, age, birth_year, email):
        self.id = id
        self.age = age
        self.birth_year = birth_year
        self.email = email

client = Client(12179707622, 20, 2004, 'o.augusto.brito@gmail.com')
print(vars(client))