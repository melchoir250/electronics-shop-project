import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture   # я не пойму он нуэен тут или нет
def all_price_phone():
    '''сравнение общей цены товара в магазине'''
    item = Item("MobilePhone", 12000, 10)
    total_price = item.calculate_total_price()
    assert total_price == 120000



def price_item():
    item = Item("MacBook", 99000, 1)
    assert item.name == 'MacBook'
    assert item.price < 100000   # проверим что цена менее 100.000
    assert item.quantity > 0   # проверим что товар есть в наличии



def discount_price_phone():
    '''сравнение скидки на товар'''
    item = Item("Iphone", 100000, 5)
    item.pay_rate = 0.7
    item.apply_discount()
    assert item.price == 70000


if __name__ == '__main__':
    all_price_phone()
    price_item()
    discount_price_phone()



# python -m tests.test_item    именно так удалось запустить в VSC
# pytest -m tests.test_item    именно так удалось запустить в VSC