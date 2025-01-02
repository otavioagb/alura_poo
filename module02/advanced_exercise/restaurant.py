class Restaurant:

    def __init__(self, name='', category='', active=True, stars=0, acessibility=True):
        self.name = name
        self.category = category
        self.active = active
        self.stars = stars
        self.acessibility = acessibility

    def __str__(self):
        return f'Restaurant: {self.name} | Category: {self.category}'


restaurant = Restaurant('OutBack', 'General', active=True, stars=5, acessibility=True)
print(restaurant)