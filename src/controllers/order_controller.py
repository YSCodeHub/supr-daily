class OrderController(object):

    def __init__(self, order_service):
        self._order_service = order_service()

    def add_order(self, id, user, items, quantities):
        self._order_service.add_order(id, user, items, quantities)
