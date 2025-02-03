from views.admin_view import AdminView

class AdminController:
    def __init__(self, statistics):
        self.statistics = statistics
        self.view = AdminView()

    def display_statistics(self, cost_per_pizza):
        self.view.display_statistics(self.statistics, cost_per_pizza)
