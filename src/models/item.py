class Item(object):
    def __init__(self):
        self._id = None
        self._name = None
        self._category = None

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_category(self, category):
        self._category = category

    def get_category(self):
        return self._category
