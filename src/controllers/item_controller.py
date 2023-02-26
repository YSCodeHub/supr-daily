class ItemController(object):
    def __init__(self, item_service):
        self._item_service = item_service()

    def add_item(self, id, name, category):
        self._item_service.add_item(id, name, category)

