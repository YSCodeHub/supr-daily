from src.services.category_service_interface import CategoryServiceInterface
from src.models.category import Category


class CategoryService(CategoryServiceInterface):
    category_details = {}

    def add_category(self, id, name, category_threshold):
        category = Category()
        category.set_id(id)
        category.set_name(name)
        category.set_category_threshold(category_threshold)
        self.__class__.category_details[id] = category
        return category

    def category_balance_per_date(self, id, date):
        for category_id in self.category_details:
            if self.category_details[category_id].get_name() == id:
                category = self.category_details.get(category_id)
                threshold = category.get_category_threshold_for_date(date)
                if threshold:
                    return threshold

    def update_category_balance_per_date(self, id, date, quantity):
        for category_id in self.category_details:
            if category_id == id:
                category = self.category_details.get(id)
                category.reduce_item_details(date, quantity)
