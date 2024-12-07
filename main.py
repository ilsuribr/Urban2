sides_count = 3


def is_valid_sides(*args):
    list_ = []

    if all(x >= 0 and isinstance(x, int) for x in args) and sides_count == len(args):
        list_ = list(args).copy()

    return list_


print(is_valid_sides(1, 2, 3))
