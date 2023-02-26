class Order(object):
    def __init__(self):
        self._id = None
        self._user = None
        self._items = {}

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_user(self, user):
        self._user = user

    def get_name(self):
        return self._user

    def add_items(self, item, quantity):
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity