from models.article import Article
from views.article_view import ArticleView

class ArticleController:
    def __init__(self):
        self.model = Article("", "", 0, "", "")
        self.view = ArticleView()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                self.create_article()
            elif choice == '2':
                self.display_article_info()
            elif choice == '3':
                break
            else:
                print("Неправильный выбор.")

    def create_article(self):
        title = input("Введите название статьи: ")
        author = input("Введите автора статьи: ")
        char_count = int(input("Введите количество символов: "))
        publication = input("Введите название издания или сайта: ")
        description = input("Введите краткое описание: ")

        self.model.set_title(title)
        self.model.set_author(author)
        self.model.set_char_count(char_count)
        self.model.set_publication(publication)
        self.model.set_description(description)

    def display_article_info(self):
        self.model.display_article_info()
