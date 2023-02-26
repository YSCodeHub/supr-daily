from src.services.order_service_interface import OrderServiceInterface
from src.models.order import Order


class OrderService(OrderServiceInterface):
    order_details = {}

    def add_order(self, id, user, items, quantities):
        order = Order()
        order.set_id(id)
        order.set_user(user)
        for item, quantity in zip(items, quantities):
            order.add_items(item, quantity)
        self.__class__.order_details[id] = order
        return order
