import os

class JunkItem:
    def __init__(self, name: str, quantity: int, value: float):
        self.name = name
        self.quantity = quantity
        self.value = value

    def __repr__(self):
        return f"JunkItem(name='{self.name}', quantity={self.quantity}, value={self.value})"


class JunkStorage:
    @staticmethod
    def serialize(items: list, filename: str):
        filepath = os.path.join("PythonLabs", "cleaning", filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in items:
                line = f"{item.name}|{item.quantity}|{str(item.value).replace('.', ',')}\n"
                f.write(line)

    @staticmethod
    def parse(filename: str) -> list:
        filepath = os.path.join("PythonLabs", "cleaning", filename)
        items = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split('|')
                if len(parts) != 3:
                    print(f"Error! line {i} skipped, amount of lines is wrong {line}")
                    continue

                name, q_str, v_str = parts
                try:
                    quantity = int(q_str)
                    value = float(v_str.replace(',', '.'))
                except ValueError:
                    print(f"Error! line {i} skipped, value or quantity is wrong {line}")
                    continue

                items.append(JunkItem(name, quantity, value))
        return items

items = [
    JunkItem("Бляшанка", 5, 2.5),
    JunkItem("Стара плата", 3, 7.8),
    JunkItem("Купка дротів", 10, 1.6)
]

filename = "junk_storage.txt"

def read(items, filename):
    
    user_input = input('read/write : ')
    if user_input == 'write':
        JunkStorage.serialize(items, filename)
        print("Items wrote down")
    elif user_input == 'read':
        restored = JunkStorage.parse(filename)
        print("\nItems got")
        for item in restored:
            print(item)
    else:
        print('wrong input')
read(items, filename)