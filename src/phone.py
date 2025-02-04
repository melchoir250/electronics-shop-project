from src.item import Item

class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        if number_of_sim <= 0:
            raise ValueError("Кол-во симкарт в телефоне не может быть менее 0")
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

