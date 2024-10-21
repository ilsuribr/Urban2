first = 1
second = 2
third = 3

if first == second and first == third:
    print(3)
elif first != second and first == third:
    print(2)
elif first == second and first != third:
    print(2)
elif first != second and first != third and second == third:
    print(2)
elif first != second and first != third and second != third:
    print(0)