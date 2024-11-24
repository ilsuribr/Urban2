x, n = (50, 5)

i = 1
list_ = []
while len(list_) < n:
    if i % x == 0:
        list_.append(i)
    i += 1

print(list_)
print([i * x for i in range(1, n + 1)])