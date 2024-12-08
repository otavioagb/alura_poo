class Restaurante:

    name = ''
    category = 'Italiana'
    active = True


italian_food = Restaurante
categoria = (italian_food.category)
print(categoria)
if italian_food.active:
    print('The restaurant is active')
else:
    print('The restaurant is inactive')
italian_food.name = 'Bistrô'


