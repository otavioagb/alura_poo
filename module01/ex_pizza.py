class PizzaResturant:

    name = 'Pizza Place'
    category = 'Fast Food'
    active = False


pizza = PizzaResturant
print(pizza.category)
pizza.active = True
print(vars(pizza.name, pizza.category, pizza.active))