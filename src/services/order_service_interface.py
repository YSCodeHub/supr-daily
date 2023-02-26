import abc


class OrderServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_order(self, id, user, items, qauntities):
        pass
