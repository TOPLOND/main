class MenuView:
    def display_menu(self, pizzas, toppings):
        print("Меню пиццерии:")
        for pizza in pizzas:
            print(pizza)
        print("\nДоступные топпинги:")
        for topping in toppings:
            print(topping)
