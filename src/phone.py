from src.item import Item


class Phone(Item):

    def __init__(self, __name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(__name, price, quantity)
        self.number_of_sim = None
        self.check_number_of_sim(number_of_sim)

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            return "This operation doesn't callable"

    def check_number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            report = "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
            return report

