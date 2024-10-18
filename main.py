my_dict = {'Владимир':1990, 'Василий':1995, 'Михаил':1989}

print('Dict:', my_dict)
print('Value:', my_dict.get('Владимир'))
print('Value:', my_dict.get('Антон'))
my_dict.update({'Антон':2000, 'Елена':2005})
print('Deleted value:', my_dict.pop('Владимир'))
print('Dict:', my_dict)

my_set = {1, 1, 2, 2, True, False, False, 'a', 'b', 'a'}

print('Set:', my_set)
my_set.add(4)
my_set.add('string')
my_set.discard(False)
print('Set modified:', my_set)