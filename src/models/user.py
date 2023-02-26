class User(object):
    def __init__(self):
        self._id = None
        self._name = None
        self._orders = []

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def add_order(self, order):
        if order not in self._orders:
            self._orders.append(order)
