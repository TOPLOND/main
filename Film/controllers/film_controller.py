from models.film import Film
from views.film_view import FilmView

class FilmController:
    def __init__(self):
        self.model = Film("", "", "", 0, 0, "", [])
        self.view = FilmView()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                self.create_film()
            elif choice == '2':
                self.display_film_info()
            elif choice == '3':
                break
            else:
                print("Неправильный выбор.")

    def create_film(self):
        title = input("Введите название фильма: ")
        genre = input("Введите жанр: ")
        director = input("Введите режиссёра: ")
        year = self.get_valid_integer("Введите год выпуска: ")
        duration = self.get_valid_integer("Введите длительность в минутах: ")
        studio = input("Введите киностудию: ")
        actors = []
        num_actors = self.get_valid_integer("Введите количество актёров: ")
        for _ in range(num_actors):
            fullname = input("Введите ФИО актёра: ")
            role = input("Введите роль актёра: ")
            actors.append({"ФИО": fullname, "роль": role})

        self.model.set_title(title)
        self.model.set_genre(genre)
        self.model.set_director(director)
        self.model.set_year(year)
        self.model.set_duration(duration)
        self.model.set_studio(studio)
        self.model.set_actors(actors)

    def get_valid_integer(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Пожалуйста, введите целое число.")

    def display_film_info(self):
        self.model.display_film_info()
