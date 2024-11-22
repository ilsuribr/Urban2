class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        raise TypeError("Можно cравнивать только объекты типа House")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        raise TypeError("Можно cравнивать только объекты типа House")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        raise TypeError("Можно cравнивать только объекты типа House")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        raise TypeError("Можно cравнивать только объекты типа House")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        raise TypeError("Можно cравнивать только объекты типа House")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        raise TypeError("Можно cравнивать только объекты типа House")

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        raise TypeError("Можно складывать только с типом int")

    def __radd__(self, value):
        return self + value


house1 = House('Акварель', 20)
house2 = House('Элитный', 30)

print(house1)
print(house2)

print(house1 == house2)  # __eq__

house1 = house1 + 10 # __add__
print(house1)

house1 += 10 # __iadd__
print(house1)

house2 = 10 + house2 # __radd__
print(house2)

print(house1 > house2)  # __gt__
print(house1 >= house2)  # __ge__
print(house1 < house2)  # __lt__
print(house1 <= house2)  # __le__
print(house1 != house2)  # __ne__
