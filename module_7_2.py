info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name: str, strings: list[str]) -> dict:
    with open(file_name, 'w', encoding='utf-8') as file:
        result_dict = {}
        line_number = 0
        for text in strings:
            result_dict[(line_number := line_number + 1, file.tell())] = text
            file.write(text + '\n')

    return result_dict


result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
