class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_genre(self):
        return self.genre

    def set_genre(self, new_genre):
        self.genre = new_genre

    def get_director(self):
        return self.director

    def set_director(self, new_director):
        self.director = new_director

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

    def get_duration(self):
        return self.duration

    def set_duration(self, new_duration):
        self.duration = new_duration

    def get_studio(self):
        return self.studio

    def set_studio(self, new_studio):
        self.studio = new_studio

    def get_actors(self):
        return self.actors

    def set_actors(self, new_actors):
        self.actors = new_actors

    def display_film_info(self):
        print(f"Название фильма: {self.title}")
        print(f"Жанр: {self.genre}")
        print(f"Режиссёр: {self.director}")
        print(f"Год выпуска: {self.year}")
        print(f"Длительность: {self.duration} минут")
        print(f"Киностудия: {self.studio}")
        print("Актёры:")
        for actor in self.actors:
            print(f"- {actor['ФИО']}: {actor['роль']}")
