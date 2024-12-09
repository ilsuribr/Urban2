class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read()
                for ch in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.lower().replace(ch, '')
                all_words[file_name] = text.split()

        return  all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for k, v in all_words.items():
            for i in range(len(v)):
                if word.lower() == v[i]:
                    result[k] = i + 1
                    break

        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for k, v in all_words.items():
            count = 0
            for i in range(len(v)):
                if word.lower() == v[i]:
                    count += 1
            result[k] = count

        return result



finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

