def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except TypeError as exc:
        return f'Ошибка "{exc}" \nПри сложении: {str(a)} + {str(b)}\n'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))