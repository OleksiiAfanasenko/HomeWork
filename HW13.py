class Human:
    def __init__(self, name: str, surname: str, age: int, phone: int, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def call(self, phone_number):
        return f'{self.phone} вызывает абонента {phone_number}.'

    def get_info(self):
        return {"name": self.name, "surname": self.surname, "age": self.age, "phone": self.phone, "address": self.address}


petr = Human('Petr', 'Petrov', 27, 80501111111, 'Kyiv, av. Peremohy 1-08')
ivan = Human('Ivan', 'Ivanov', 28, 80501111112, 'Kyiv, av. Peremohy 1 -09')
oleksandr = Human('Oleksandr', 'Oleksandrov', 29, 80501111113, 'Kyiv, av.Peremohy 1-10')

petr.get_info()
ivan.get_info()
oleksandr.get_info()

