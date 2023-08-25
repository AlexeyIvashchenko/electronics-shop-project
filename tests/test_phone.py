import os
import csv
from src.phone import Phone


def test_init():
    phone = Phone("iPhone", 80000, 5, 2)
    assert phone.name == "iPhone"
    assert phone.price == 80000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_repr():
    phone = Phone("iPhone", 80000, 5, 2)
    assert repr(phone) == "Phone('iPhone', 80000, 5, 2)"


def test_add():
    phone1 = Phone("Phone 1", 100, 3, 1)
    phone2 = Phone("Phone 2", 150, 2, 2)
    result = phone1 + phone2
    assert result == 5


def test_check_number_of_sim_positive():
    phone = Phone("Phone", 200, 1, 2)
    assert phone.number_of_sim == 2


def test_check_number_of_sim_negative():
    phone = Phone("Phone", 200, 1, -1)
    assert phone.number_of_sim is None
