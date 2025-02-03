class Article:
    def __init__(self, title, author, char_count, publication, description):
        self.title = title
        self.author = author
        self.char_count = char_count
        self.publication = publication
        self.description = description

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_author(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author

    def get_char_count(self):
        return self.char_count

    def set_char_count(self, new_char_count):
        self.char_count = new_char_count

    def get_publication(self):
        return self.publication

    def set_publication(self, new_publication):
        self.publication = new_publication

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def display_article_info(self):
        print(f"Тема статьи: {self.title}")
        print(f"Автор статьи: {self.author}")
        print(f"Количество символов: {self.char_count}")
        print(f"Название издания или сайта: {self.publication}")
        print(f"Краткое описание: {self.description}")
