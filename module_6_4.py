import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_color(*color):
            self.__color = list(color).copy()
        else:
            self.__color = [0] * 3

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides).copy()
        else:
            self.__sides = [1] * self.sides_count

        self.filled = False

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(x in range(256) for x in (r, g, b))

    def __is_valid_sides(self, *args):
        return all(x >= 0 and isinstance(x, int) for x in args) and self.sides_count == len(args)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides).copy()

    def __len__(self):
        result = 0
        for i in self.get_sides():
            result += i

        return result


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__len__() / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __is_valid_sides(self, *args):

        if all(x >= 0 and isinstance(x, int) for x in args) and self.sides_count == len(args):
            a = args[0]
            b = args[1]
            c = args[2]
            if not (a + b <= c or a + c <= b or b + c <= a):
                return True

        return False

    def get_square(self):
        sides_list = self.get_sides()

        if self.__is_valid_sides(*sides_list):
            p = sum(sides_list) / 2
            return (p * (p - sides_list[0]) * (p - sides_list[1]) * (p - sides_list[2])) ** 0.5
        else: return 'Error'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 5, 5, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
print(circle1.get_square())
print(triangle1.get_square())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
