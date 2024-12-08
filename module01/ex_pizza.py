class PizzaResturant:

    name = 'Pizza Place'
    category = 'Fast Food'
    active = False


pizza = PizzaResturant
print(pizza.category)
pizza.active = True
print(pizza.name,'\n', pizza.category,'\n', pizza.active)