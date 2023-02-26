

class UserController(object):
    def __init__(self, user_service):
        self._user_service = user_service()

    def add_user(self, id, name, orders):
        self._user_service.add_user(id, name, orders)

    def add_order(self, id, order):
        self._user_service.add_order(id, order)
