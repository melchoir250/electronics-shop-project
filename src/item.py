import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self._name = name
        else:
            self._name = name[:10]


    @classmethod
    def instantiate_from_csv(cls):
        csv_items = '/Users/vlad/Desktop/Python/electronics-shop-project/src/items.csv'
        created_items = []
        with open(csv_items, newline='') as csvfile:
            lines = csv.DictReader(csvfile)
            for line in lines:
                #if 'name' in line and 'price' in line and 'quantity' in line:
                name = line['name'].strip()
                price = float(line['price'].strip())
                quantity = int(line['quantity'].strip())
                item = cls(name, price, quantity)
                created_items.append(item)
        return created_items
        #print(len(created_items))


    @staticmethod
    def string_to_number(value:str) -> float:
        return float(value)



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
