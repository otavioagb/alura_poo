class Restaurant:

    name = ''
    category = 'Italian'
    active = True


italian_food = Restaurant
category = (italian_food.category)
print(category)
if italian_food.active:
    print('The restaurant is active')
else:
    print('The restaurant is inactive')
italian_food.name = 'Tagliatella'


