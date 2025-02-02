from models.pizza import Pizza
from models.topping import Topping
from views.menu_view import MenuView

class MenuController:
    def __init__(self):
        self.pizzas = [
            Pizza("Маргарита", 300, ["Тесто", "Соус", "Сыр", "Томаты"]),
            Pizza("Пепперони", 350, ["Тесто", "Соус", "Сыр", "Пепперони"]),
        ]
        self.toppings = [
            Topping("Грибы", 50),
            Topping("Оливки", 40),
        ]
        self.view = MenuView()

    def display_menu(self):
        self.view.display_menu(self.pizzas, self.toppings)
