import unittest
from src.item import Item  # Замените "your_module_name" на имя вашего модуля

class TestItemClass(unittest.TestCase):

    def setUp(self):
        # Подготовка данных для тестов
        self.item1 = Item("Product A", 10.0, 5)
        self.item2 = Item("Product B", 20.0, 3)

    def test_name_shortening(self):
        # Проверка, что имя товара укорачивается до 10 символов
        self.assertEqual(self.item1.name, "Product A")
        self.assertEqual(self.item2.name, "Product B")

        # Проверка, что длинное имя обрезается до 10 символов
        long_name = "ThisIsALongProductName"
        long_item = Item(long_name, 15.0, 2)
        self.assertEqual(long_item.name, long_name[:10])

    def test_total_price_calculation(self):
        # Проверка правильности расчета общей стоимости товара
        self.assertEqual(self.item1.calculate_total_price(), 50.0)  # 10.0 * 5
        self.assertEqual(self.item2.calculate_total_price(), 60.0)  # 20.0 * 3

    def test_apply_discount(self):
        # Проверка применения скидки
        self.item1.pay_rate = 0.9  # 10% скидка
        self.item1.apply_discount()
        self.assertEqual(self.item1.price, 9.0)  # 10.0 * 0.9

        self.item2.pay_rate = 0.8  # 20% скидка
        self.item2.apply_discount()
        self.assertEqual(self.item2.price, 16.0)  # 20.0 * 0.8

if __name__ == '__main__':
    unittest.main()


# python -m tests.test_item    именно так удалось запустить в VSC
# pytest -m tests.test_item    именно так удалось запустить в VSC