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


    def is_valid(self):  # Оголошення методу для перевірки валідності номера телефону
    return len(self.value) == 10 and self.value.isdigit()  # Повертає True, якщо довжина номера телефону дорівнює 10 і всі символи є цифрами, інакше повертає False


class Record:  # Оголошення класу Record
    def __init__(self, name):  # Оголошення конструктора класу з аргументом name
        self.name = Name(name)  # Створення об'єкту класу Name з переданим ім'ям
        self.phones = []  # Ініціалізація порожнього списку для зберігання телефонів

    def add_phone(self, phone):  # Оголошення методу для додавання телефону до запису
        self.phones.append(Phone(phone))  # Додавання нового телефону до списку телефонів запису

    def remove_phone(self, phone):  # Оголошення методу для видалення телефону з запису
        self.phones = [p for p in self.phones if p.value != phone]  # Видалення телефону зі списку телефонів запису, якщо він співпадає з переданим

    def edit_phone(self, old_phone, new_phone):  # Оголошення методу для редагування телефону
        for p in self.phones:  # Ітерація по всіх телефонах запису
            if p.value == old_phone:  # Якщо знайдено телефон, який потрібно змінити
                p.value = new_phone  # Заміна старого значення телефону на нове
                break  # Виходимо з циклу після зміни

    def find_phone(self, phone):  # Оголошення методу для пошуку телефону в записі
        for p in self.phones:  # Ітерація по всіх телефонах запису
            if p.value == phone:  # Якщо знайдено шуканий телефон
                return p  # Повертаємо його
        return None  # Повертаємо None, якщо телефон не знайдено

    def __str__(self):  # Оголошення методу для конвертації об'єкту в рядок
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"  # Повертає рядок з ім'ям та списком телефонів запису



class AddressBook(UserDict):  # Оголошення класу AddressBook, що успадковує клас UserDict
    def add_record(self, record):  # Оголошення методу для додавання запису до адресної книги
        self.data[record.name.value] = record  # Додавання запису до словника адресної книги, використовуючи ім'я як ключ

    def find(self, name):  # Оголошення методу для пошуку запису за ім'ям у адресній книзі
        return self.data.get(name)  # Повернення запису за вказаним ім'ям, якщо він існує у книзі

    def delete(self, name):  # Оголошення методу для видалення запису за ім'ям з адресної книги
        if name in self.data:  # Перевірка, чи ім'я присутнє у книзі
            del self.data[name]  # Видалення запису з книги, якщо воно присутнє

    def __str__(self):  # Оголошення методу для конвертації об'єкту в рядок
        return "\n".join(str(record) for record in self.data.values())  # Повертає рядок, складений з рядків, які представляють кожен запис у словнику адресної книги

    

