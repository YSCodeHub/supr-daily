from src.services.item_service_interface import ItemServiceInterface
from src.models.item import Item


class ItemService(ItemServiceInterface):
    item_details = {}

    def add_item(self, id, name, category):
        item = Item()
        item.set_id(id)
        item.set_name(name)
        item.set_category(category)
        self.__class__.item_details[id] = item
        return item
