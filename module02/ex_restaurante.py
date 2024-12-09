class Restaurante:

    def __init__(self, name, category, active, stars, acessibility):
        self.name = name
        self.category = category
        self.active = active
        self.stars = stars
        self.acessibility = acessibility

    def __str__(self):
        return f'Restaurante: {self.name} | Categoria: {self.category}'


restaurant = Restaurante('OutBack', 'General', active=True, stars=5, acessibility=True)
print(restaurant)