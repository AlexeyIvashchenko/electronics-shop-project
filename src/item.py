import csv
import os


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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return "This operation doesn't callable"

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate
        return self.price

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
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, "items.csv")

        counter = 1
        with open(file_path, newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                example = Item(row['name'], row['price'], row['quantity'])
                counter += 1

    @staticmethod
    def string_to_number(s):
        return int(float(s))
