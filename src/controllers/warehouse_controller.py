class WareHouseController(object):
    def __init__(self, warehouse_service):
        self._warehouse_service = warehouse_service()

    def add_warehouse(self, id, items_details):
        return self._warehouse_service.add_warehouse(id, items_details)

    def get_warehouse_item_balance(self, id, item):
        return self._warehouse_service.get_warehouse_item_balance(id, item)

    def update_warehouse_item_balance(self, id, item, quantity):
        self._warehouse_service.update_warehouse_item_balance(id, item, quantity)
