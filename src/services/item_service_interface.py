import abc


class ItemServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_item(self, id, name, category):
        pass
