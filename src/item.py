from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, __name: str, price: float, quantity: int) -> None:
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        return self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
            return
        else:
            self.__name = name[:10]
            return

    @classmethod
    def instantiate_from_csv(cls):
        counter = 1
        file = "items.csv"
         with open("items.csv", "r") as file:
            cls.name, cls.price, cls.quantity = file.readline(counter).split(',')
        if counter == 5:
            counter = 1
        else:
            counter += 1

    @staticmethod
    def string_to_number():
        return int(all)
