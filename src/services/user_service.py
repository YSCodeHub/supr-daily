from src.services.user_service_interface import UserServiceInterface
from src.models.user import User


class UserService(UserServiceInterface):
    user_details = {}

    def add_user(self, id, name, orders):
        user = User()
        user.set_id(id)
        user.set_name(name)
        for order in orders:
            user.add_order(order)
        self.__class__.user_details[id] = user
        return user

    def add_order(self, user_id, order):
        user = self.__class__.user_details[user_id]
        user.add_order(order)
        self.__class__.user_details[user_id] = user
