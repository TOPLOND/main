from models.order import Order
from views.order_view import OrderView

class OrderController:
    def __init__(self, menu_controller, statistics):
        self.menu_controller = menu_controller
        self.statistics = statistics
        self.view = OrderView()

    def create_order(self, pizza_index, topping_indices):
        pizza = self.menu_controller.pizzas[pizza_index]
        toppings = [self.menu_controller.toppings[i] for i in topping_indices]
        order = Order(pizza, toppings)
        self.statistics.add_order(order)
        self.view.display_order(order)
