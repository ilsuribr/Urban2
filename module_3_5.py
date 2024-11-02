def get_multiplied_digits(number):
    if len(str(number)) == 1:
        return number
    else:
        return int(str(number)[0]) * get_multiplied_digits(int(str(number)[1:]))


print(get_multiplied_digits(123))
