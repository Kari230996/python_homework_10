'''
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
'''


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, *args):
        if animal_type == 'Cat':
            return Cat(name, *args)
        elif animal_type == 'Dog':
            return Dog(name, *args)
        elif animal_type == 'Bird':
            return Bird(name, *args)
        else:
            raise ValueError(f'Неизвестный тип животного: {animal_type}')


class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        pass


class Cat(Animal):
    def __init__(self, name, sleep_time):
        super().__init__(name)
        self.sleep_time = sleep_time

    def info(self):
        return f'Мой кот {pet_1.name} дрыхнул целых {pet_1.sleep_time} часов!'


class Dog(Animal):
    def __init__(self, name, command):
        super().__init__(name)
        self.command = command

    def info(self):
        return f'Моя собака {pet_2.name} знает команду "{pet_2.command}".'


class Bird(Animal):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def info(self):
        return f'Мой {pet_3.name} поёт песню "{pet_3.song}".'


animal_factory = AnimalFactory()
pet_1 = animal_factory.create_animal('Cat', 'Байсюнк', 20)
pet_2 = animal_factory.create_animal('Dog', 'Джек', 'Дай лапу')
pet_3 = animal_factory.create_animal('Bird', 'Немо', 'My Heart will go on')


print(pet_1.info())
print(pet_2.info())
print(pet_3.info())
