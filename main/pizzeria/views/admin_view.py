class AdminView:
    def display_statistics(self, statistics, cost_per_pizza):
        print(f"Продано пицц: {statistics.get_total_pizzas_sold()}")
        print(f"Выручка: {statistics.get_total_sales()} руб.")
        print(f"Прибыль: {statistics.get_profit(cost_per_pizza)} руб.")
