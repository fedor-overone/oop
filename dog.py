class Dog:
    """ Класс для создания экземпляров класса Dog """

    # атрибут класса, общий для всех созданных экземпляров будет считать количество созданных собак
    dog_count = 0

    # Магический метод __init__ запускается при каждом создании нового экземпляра на основе класса
    # __init__ вызывает конструктор класса
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.dog_count += 1
        print(f"Создан новый экземпляр класса Dog: имя {self.name}, возраст {self.age}")
        print(f"Всего собак создано {Dog.dog_count}")
        print("---------------------------")

    # self - служебное слово, куда будет передаваться созданный в далнейшем экземпляр класса
    # например вместо self.name будет dog1.name, dog2.name

    def bark(self):
        print("bark")

    # геттеры и сеттеры для получения и изменения  атрибутов класса
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


dog1 = Dog("Барбос", 4)
dog2 = Dog("Шарик", 5)

print(f"Возраст собаки {d1.name}", d1.age)
dog1.set_name("Рекс")
print(f"Новое имя собаки - {d1.name}")

print("Суммарное число собак:", Dog.dog_count)

