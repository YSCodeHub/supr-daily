class Category(object):
    def __init__(self):
        self._id = None
        self._name = None
        self._category_threshold_details = {}

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_category_threshold(self, details):
        self._category_threshold_details = details

    def get_category_threshold_for_date(self, date):
        if date in self._category_threshold_details:
            return self._category_threshold_details[date]

    def reduce_item_details(self, date, quantity):
        if date in self._category_threshold_details:
            self._category_threshold_details[date] -= quantity
