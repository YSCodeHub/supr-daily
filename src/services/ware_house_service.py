from src.services.ware_house_service_interface import WareHouseServiceInterface
from src.models.ware_house import WareHouse


class WareHouseService(WareHouseServiceInterface):
    warehouse_details = {}

    def add_warehouse(self, id, items_details):
        warehouse = WareHouse()
        warehouse.set_id(id)
        for item_detail in items_details:
            warehouse.add_item_details(item_detail)
        self.__class__.warehouse_details[id] = warehouse
        return warehouse

    def get_warehouse_item_balance(self, id, item):
        for warehouse_id in self.warehouse_details:
            if warehouse_id == id:
                warehouse = self.warehouse_details.get(id)
                item_details = warehouse.get_item_details(item)
                if item_details:
                    return item_details[1]

    def update_warehouse_item_balance(self, id, item, quantity):
        for warehouse_id in self.warehouse_details:
            if warehouse_id == id:
                warehouse = self.warehouse_details.get(id)
                warehouse.reduce_item_details(item, quantity)
