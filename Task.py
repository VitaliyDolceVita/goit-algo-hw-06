from collections import UserDict   # Імпортуєм необхідну функцію модуля


class Field:   # Створюємо клас Field
    def __init__(self, value):  # Ініціація класу
        self.value = value  # Присвоєння значення атрибуту value

    def __str__(self):  # Оголошення методу для конвертації об'єкта в рядок 
        return str(self.value)  


class Name(Field):  # Створюєм клас Name який наслідує клас  Field
    def __init__(self, name):
        self.name = name


class Phone(Field):   # Створюєм клас Name який наслідує клас  Field
    def __init__(self, value):  # Оголошення конструктора класу з аргументом value
        super().__init__(value)  # Виклик конструктора батьківського класу Field з передачею значення value
        if not self.is_valid():
            raise ValueError("Invalid phone number format. Please provide a 10-digit phone number.")  # виклик винятку, якщо номер телефону некоректний

    def is_valid(self):
        return len(self.value) == 10 and self.value.isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


