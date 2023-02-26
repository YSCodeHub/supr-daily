import abc


class UserServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_user(self, id, name, orders):
        pass

    @abc.abstractmethod
    def add_order(self, user, order):
        pass
