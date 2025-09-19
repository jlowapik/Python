from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name: str, quantity: int, price: float) -> None:
        if not isinstance(name, str):
            return 'Incorrect data'
        if not isinstance(quantity, int):
            return 'Incorrect data'
        if not isinstance(price, float):
            return 'Incorrect data'

        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def requires_prescription(self) -> bool:
        pass
    @abstractmethod
    def storage_requirments(self) -> str:
        pass
    def total_price(self) -> float:
        return self.quantity * self.price
    @abstractmethod
    def info(self) -> str:
        pass

class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True
    def storage_requirments(self) -> str:
        return '8-15 C, Темне місце'
    def info(self) -> str:
        return f'Антибіотик: {self.name}, кількість: {self.quantity}, ціна: {self.price}, ціна за замовлення: {self.total_price():.2f}, рецепт: {self.requires_prescription()}, умови зберігання: {self.storage_requirments()}'
    
class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False
    def storage_requirments(self) -> str:
        return '15-25 C, cухе місце'
    def info(self) -> str:
        return f'Вітамін: {self.name}, кількість: {self.quantity}, ціна: {self.price}, ціна за замовлення: {self.total_price():.2f}, рецепт: {self.requires_prescription()}, умови зберігання: {self.storage_requirments()}'

class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True
    def storage_requirments(self) -> str:
        return '2-8 C, Холодильник'
    def info(self) -> str:
        return f'Вакцина: {self.name}, кількість: {self.quantity}, ціна: {self.price}, ціна за замовлення: {self.total_price() * 1.1:.2f}, рецепт: {self.requires_prescription()}, умови зберігання: {self.storage_requirments()}'


