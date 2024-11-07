def calculate_structure_sum_re(data_structure):  # с помощью регулярных выражений и исключения
    import re
    list_ = re.findall(r'[a-zA-Z0-9]+', str(data_structure))
    sum = 0
    for i in list_:
        try:
            sum += int(i)
        except:
            sum += len(i)
    return sum


def calculate_structure_sum_rec(data_structure): # с помощью рекурсии
    if data_structure == '' or data_structure is None:
        return 0
    elif isinstance(data_structure, int):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, list):
        if len(data_structure) == 0:
            return 0
        elif len(data_structure) == 1:
            return calculate_structure_sum_rec(data_structure[0])
        else:
            return calculate_structure_sum_rec(data_structure[0]) + calculate_structure_sum_rec(data_structure[1:])
    elif isinstance(data_structure, tuple):
        if len(data_structure) == 0:
            return 0
        elif len(data_structure) == 1:
            return calculate_structure_sum_rec(data_structure[0])
        else:
            return calculate_structure_sum_rec(data_structure[0]) + calculate_structure_sum_rec(data_structure[1:])
    elif isinstance(data_structure, set):
        if len(data_structure) == 0:
            return 0
        elif len(data_structure) == 1:
            return calculate_structure_sum_rec(list(data_structure)[0])
        else:
            return (calculate_structure_sum_rec(list(data_structure)[0]) +
                    calculate_structure_sum_rec(list(data_structure)[1:]))
    elif isinstance(data_structure, dict):
        if len(data_structure) == 0:
            return 0
        elif len(data_structure) == 1:
            return (calculate_structure_sum_rec(list(data_structure.keys())[0]) +
                    calculate_structure_sum_rec(list(data_structure.values())[0]))
        else:
            return (calculate_structure_sum_rec(list(data_structure.keys())[0]) +
                    calculate_structure_sum_rec(list(data_structure.keys())[1:]) +
                    calculate_structure_sum_rec(list(data_structure.values())[0]) +
                    calculate_structure_sum_rec(list(data_structure.values())[1:]))



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum_re(data_structure)
print(result)

result = calculate_structure_sum_rec(data_structure)
print(result)
