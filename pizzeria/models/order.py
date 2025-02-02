class Order:
    def __init__(self, pizza, toppings=None):
        self.pizza = pizza
        self.toppings = toppings if toppings else []
        self.total_price = pizza.price + sum(topping.price for topping in self.toppings)

    def __str__(self):
        toppings_str = ', '.join(str(topping) for topping in self.toppings)
        return f"Pizza: {self.pizza}, Toppings: {toppings_str}, Total: {self.total_price} руб."
