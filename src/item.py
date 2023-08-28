import csv
import os

csv_items = os.path.join(os.path.dirname(__file__), 'items.csv')


class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        """
        Pеализуйте возможность сложения экземпляров класса `Phone` и `Item` (сложение по количеству товара в магазине)
        """
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты Item и дочерние объекты")
        else:
            return self.quantity + other.quantity


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []

        created_items = []
        with open(csv_items, newline='', encoding = 'cp1251') as csvfile:
            lines = csv.DictReader(csvfile)
            for line in lines:
                name = line['name'].strip()
                price = float(line['price'].strip())
                quantity = int(line['quantity'].strip())
                item = cls(name, price, quantity)
                created_items.append(item)


    @staticmethod
    def string_to_number(value:str) -> float:
        return int(float(value))



