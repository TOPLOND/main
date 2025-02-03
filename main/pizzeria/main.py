from controllers.menu_controller import MenuController
from controllers.order_controller import OrderController
from controllers.admin_controller import AdminController
from models.statistics import Statistics

def main():
    menu_controller = MenuController()
    statistics = Statistics()
    order_controller = OrderController(menu_controller, statistics)
    admin_controller = AdminController(statistics)

    while True:
        print("\n1. Показать меню")
        print("2. Сделать заказ")
        print("3. Показать статистику (только для админа)")
        print("4. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            menu_controller.display_menu()
        elif choice == '2':
            try:
                pizza_index = int(input("Выберите пиццу (индекс): "))
                topping_indices = list(map(int, input("Выберите топпинги (индексы через пробел): ").split()))
                order_controller.create_order(pizza_index, topping_indices)
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите числовые индексы.")
        elif choice == '3':
            try:
                cost_per_pizza = float(input("Введите себестоимость одной пиццы: "))
                admin_controller.display_statistics(cost_per_pizza)
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите числовое значение.")
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
