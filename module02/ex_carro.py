class Carro:

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

car = Carro('Renault Kangoo', 'White', 2008)
print(vars(car))
