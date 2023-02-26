class CategoryController(object):

    def __init__(self, category_service):
        self._category_service = category_service()

    def add_category(self, id, name, category_threshold):
        self._category_service.add_category(id, name, category_threshold)

    def category_balance_per_date(self, id, date):
        return self._category_service.category_balance_per_date(id, date)

    def update_category_balance_per_date(self, id, date, quantity):
        self._category_service.update_category_balance_per_date(id, date, quantity)
