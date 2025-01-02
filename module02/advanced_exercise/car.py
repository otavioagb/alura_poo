class Car:

    def __init__(self, model='', color='', year=0):
        self.model = model
        self.color = color
        self.year = year

car = Car('Renault Kangoo', 'White', 2008)
print(vars(car))
