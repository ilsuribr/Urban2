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
        byte_number = 0
        for text in strings:
            line_number += 1
            byte_number = file.tell()
            file.write(text + '\n')
            result_dict[(line_number, byte_number)] = text

    return result_dict


result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
