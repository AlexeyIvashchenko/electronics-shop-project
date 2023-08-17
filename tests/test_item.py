import os
import csv
from src.item import Item  # Замените на имя вашего модуля


# Тест для calculate_total_price
def test_calculate_total_price():
    item = Item("TestItem", 10.0, 3)
    assert item.calculate_total_price() == 30.0


# Тест для apply_discount
def test_apply_discount():
    item = Item("TestItem", 10.0, 3)
    assert item.apply_discount() == 10.0


# Тест для name property и setter
def test_name_property_and_setter():
    item = Item("TestItemName", 10.0, 3)
    assert item.name == "TestItemName"

    long_name = "ThisIsALongName"
    item.name = long_name
    assert item.name == long_name[:10]


# Тест для метода instantiate_from_csv
def instantiate_from_csv(cls):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "items.csv")

    items = []  # Создаем список для хранения объектов Item

    with open(file_path, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            example = Item(row['name'], row['price'], row['quantity'])
            items.append(example)  # Добавляем объект Item в список

    return items  # Возвращаем список созданных объектов Item


# Тест для метода string_to_number
def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


# Запуск тестов
if __name__ == "__main__":
    import pytest

    pytest.main()
