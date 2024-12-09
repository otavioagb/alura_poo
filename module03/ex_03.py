class Pessoa:

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def __str__(self):
        return f'Name: {self.name} | Age: {self.age} | Profession: {self.profession}'

    def aniversario(self):
        self.age += 1

    @property
    def greeting(self):
        if self.profession:
            return f'Olá, sou {self.name}! Trabalho como {self.profession}.'
        else:
            return f'Olá, sou {self.name}!'
