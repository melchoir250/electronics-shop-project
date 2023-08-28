import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def sample_item():
    return Item("Sample Item", 10.0, 5)

def test_item_instantiation(sample_item):
    assert sample_item.name == "Sample Item"
    assert sample_item.price == 10.0
    assert sample_item.quantity == 5

def test_calculate_total_price(sample_item):
    assert sample_item.calculate_total_price() == 50.0

def test_apply_discount(sample_item):
    sample_item.pay_rate = 0.8
    sample_item.apply_discount()
    assert sample_item.price == 8.0

def test_name_length_limit(sample_item):
    sample_item.name = "This is a long name"
    assert len(sample_item.name) <= 10

def test_repr(sample_item):
    expected_repr = "Item('Sample Item', 10.0, 5)"
    assert repr(sample_item) == expected_repr

def test_str(sample_item):
    assert str(sample_item) == "Sample Item"

def test___add__():
    """
    Тест на проверку правильного сложения количества товаров разных классов
    :return:
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


if __name__ == '__main__':
    pytest.main()


# python -m tests.test_item    именно так удалось запустить в VSC
# pytest -m tests.test_item    именно так удалось запустить в VSC