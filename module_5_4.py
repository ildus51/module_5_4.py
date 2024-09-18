class House:
    houses_history = []  # Атрибут класса для хранения названий созданных объектов

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # Добавляем название здания в историю при создании объекта
        House.houses_history.append(self.name)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        raise TypeError(f"Неподдерживаемый операнд: {type(other)}")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        raise TypeError(f"Неподдерживаемый операнд: {type(other)}")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        raise TypeError(f"Неподдерживаемый операнд: {type(other)}")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        raise TypeError(f"Неподдерживаемый операнд: {type(other)}")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        raise TypeError(f"Неподдерживаемый операнд: {type(other)}")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        raise TypeError(f"Неподдерживаемый операнд: {type(other)}")

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f"{self.name} снесён,но он останется в истории")

# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Проверка истории
h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Проверка истории
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Проверка истории

# Удаление объектов
del h2
del h3

print(House.houses_history)  # Проверка истории после удаления