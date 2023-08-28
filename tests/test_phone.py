from src.phone import Phone
import pytest

def test_phone_initialization():
    phone = Phone("iPhone", 999.99, 10, 2)
    assert phone.name == "iPhone"
    assert phone.price == 999.99
    assert phone.quantity == 10
    assert phone.number_of_sim == 2

def test_invalid_number_of_sim():
    with pytest.raises(ValueError):
        phone = Phone("Samsung", 799.99, 5, -1)

def test_phone_repr():
    phone = Phone("Nokia", 199.99, 8, 1)
    expected_repr = "Phone('Nokia', 199.99, 8, 1)"
    assert repr(phone) == expected_repr