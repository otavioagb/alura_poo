class Person:

    def __init__(self, name='', age=0, profession=''):
        self.name = name
        self.age = age
        self.profession = profession

    def __str__(self):
        return f'Name: {self.name} | Age: {self.age} | Profession: {self.profession}'

    def birthday(self):
        self.age += 1

    @property
    def greeting(self):
        if self.profession:
            if self.profession[0].lower() in 'aeiou':
                return f"Hello, {self.name}! You are an {self.profession}."
            return f"Hello, {self.name}! You are a {self.profession}."
        else:
            return f'Hello, {self.name}!'
        
vincent = Person('Vincent', 25, 'Engineer')
print(vincent.greeting)
