class Statistics:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_total_sales(self):
        return sum(order.total_price for order in self.orders)

    def get_total_pizzas_sold(self):
        return len(self.orders)

    def get_profit(self, cost_per_pizza):
        return self.get_total_sales() - (len(self.orders) * cost_per_pizza)
