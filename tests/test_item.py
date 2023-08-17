import pytest
from src import item
from src.item import Item


@pytest.fixture
def test_instance():
    instance = Item("Кружка", 100, 20)
    instance.price = 100.0
    instance.pay_rate = 0.9
    return instance


def test_calculate_total_price(test_instance):
    expected_total_price = test_instance.price * test_instance.pay_rate
    calculated_total_price = test_instance.calculate_total_price()
    assert calculated_total_price == expected_total_price


def test_apply_discount(test_instance):
    original_price = test_instance.price
    test_instance.apply_discount()
    new_price = test_instance.price
    assert new_price != original_price
    assert new_price == test_instance.calculate_total_price()
