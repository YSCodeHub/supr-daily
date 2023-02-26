import abc


class WareHouseServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_warehouse(self, id, _items_details):
        pass

    @abc.abstractmethod
    def get_warehouse_item_balance(self, id, item):
        pass

    @abc.abstractmethod
    def update_warehouse_item_balance(self, id, item, quantity):
        pass
