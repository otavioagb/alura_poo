# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

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