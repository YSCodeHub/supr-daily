import abc


class CategoryServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_category(self, id, name, category_threshold):
        pass

    @abc.abstractmethod
    def category_balance_per_date(self, id, date):
        pass

    @abc.abstractmethod
    def update_category_balance_per_date(self, id, date, quantity):
        pass
