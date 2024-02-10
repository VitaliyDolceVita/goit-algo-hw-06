from collections import UserDict   # Імпортуєм необхідну функцію модуля


class Field:   # Створюємо клас поле
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.is_valid():
            raise ValueError("Invalid phone number format. Please provide a 10-digit phone number.")

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


# Example usage:

# Create new address book
book = AddressBook()

# Create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John's record to address book
book.add_record(john_record)

# Create and add new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all records in the book
for name, record in book.data.items():
    print(record)

# Find and edit phone for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

# Find specific phone in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: 5555555555

# Delete Jane's record
book.delete("Jane")
