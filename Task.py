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



class AddressBook(UserDict):  # Оголошення класу AddressBook, що успадковує клас UserDict
    def add_record(self, record):  # Оголошення методу для додавання запису до адресної книги
        self.data[record.name.value] = record  # Додавання запису до словника адресної книги, використовуючи ім'я як ключ

    def find(self, name):  # Оголошення методу для пошуку запису за ім'ям у адресній книзі
        return self.data.get(name)  # Повернення запису за вказаним ім'ям, якщо він існує у книзі

    def delete(self, name):  # Оголошення методу для видалення запису за ім'ям з адресної книги
        if name in self.data:  # Перевірка, чи ім'я присутнє у книзі
            del self.data[name]  # Видалення запису з книги, якщо воно присутнє


    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


