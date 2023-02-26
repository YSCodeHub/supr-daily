class WareHouse(object):
    def __init__(self):
        self._id = None
        self._items_details = dict()

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def add_item_details(self, details):
        for item in details:
            if item in self._items_details:
                self._items_details[item] += details[item]
            else:
                self._items_details[item] = details[item]

    def get_item_details(self, item):
        if str(item) in self._items_details:
            return item, self._items_details[str(item)]

    def reduce_item_details(self, item, quantity):
        if str(item) in self._items_details:
            self._items_details[str(item)] -= quantity
