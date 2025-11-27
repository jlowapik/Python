from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import csv

@dataclass(order=True)
class Item:
    category: str
    value: float
    name: str = field(compare=False)
    quantity: int = field(compare=False)
    condition: str = field(compare=False)
    location: str = field(compare=False)
    date_added: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"), compare=False)

    def total_value(self) -> float:
        return self.quantity * self.value

    def __str__(self) -> str:
        return (f"[{self.category}] {self.name} ({self.quantity} шт.) — "
                f"{self.value} грн/шт, стан: {self.condition}")

@dataclass
class Inventory:
    items: List[Item] = field(default_factory=list)

    def add_item(self, item: Item):
        self.items.append(item)
        self.items.sort()

    def remove_item(self, name: str):
        self.items = [item for item in self.items if item.name != name]

    def find_by_category(self, category: str) -> List[Item]:
        return [item for item in self.items if item.category == category]

    def total_inventory_value(self) -> float:
        return sum(item.total_value() for item in self.items)

    def save_to_csv(self, filename: str):
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'category', 'quantity', 'value', 'condition', 'location', 'date_added'])
            for item in self.items:
                writer.writerow([item.name, item.category, item.quantity, item.value,
                                 item.condition, item.location, item.date_added])

    def load_from_csv(self, filename: str):
        with open(filename, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.items = [
                Item(
                    name=row['name'],
                    category=row['category'],
                    quantity=int(row['quantity']),
                    value=float(row['value']),
                    condition=row['condition'],
                    location=row['location'],
                    date_added=row.get('date_added', datetime.now().strftime("%Y-%m-%d"))
                )
                for row in reader
            ]
        self.items.sort()

    def export_summary(self) -> str:
        summary = {}
        for item in self.items:
            summary[item.category] = summary.get(item.category, 0) + item.quantity
        report = "Короткий звіт по категоріях:\n"
        for category, qty in summary.items():
            report += f"- {category}: {qty} шт.\n"
        return report

    def filter_items(self, **kwargs) -> List[Item]:
        result = self.items
        for key, value in kwargs.items():
            result = [item for item in result if getattr(item, key, None) == value]
        return result

    def sort_items(self, *fields):
        self.items.sort(key=lambda item: tuple(getattr(item, f) for f in fields))

def main():
    inv = Inventory()

    inv.add_item(Item(name="Гаечний ключ", category="інструменти", quantity=3, value=15.0, condition="уживаний", location="гараж"))
    inv.add_item(Item(name="Молоток", category="інструменти", quantity=2, value=25.0, condition="новий", location="комора"))
    inv.add_item(Item(name="Старий ноутбук", category="електроніка", quantity=1, value=5000.0, condition="зламаний", location="комора"))
    inv.add_item(Item(name="Акумулятор", category="електроніка", quantity=4, value=200.0, condition="уживаний", location="гараж"))
    inv.add_item(Item(name="Бляшанка", category="металобрухт", quantity=10, value=5.0, condition="уживаний", location="сарай"))

    print("=== Всі предмети ===")
    for item in inv.items:
        print(item)


    print("\n=== Інструменти ===")
    for item in inv.find_by_category("інструменти"):
        print(item)

    print(f"\nЗагальна вартість інвентарю: {inv.total_inventory_value()} грн")

    print("\n=== Фільтр: стан = уживаний ===")
    for item in inv.filter_items(condition="уживаний"):
        print(item)

    print("\n=== Звіт по категоріях ===")
    print(inv.export_summary())

    inv.save_to_csv("inventory.csv")
    print("\nІнвентар збережено у inventory.csv")

    new_inv = Inventory()

    new_inv.load_from_csv("inventory.csv")
    print("\n=== Завантажено з CSV ===")
    for item in new_inv.items:
        print(item)

    new_inv.remove_item("Молоток")
    print("\n=== Після видалення Молотка ===")
    for item in new_inv.items:
        print(item)

if __name__ == "__main__":
    main()
