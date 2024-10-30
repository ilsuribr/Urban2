def count_divisible(n: int, k: int) -> int:
    # your code here
    count = 0
    for i in range(1, n + 1):
        if i % k == 0:
            count += 1
    return count


print("Example:")
print(count_divisible(10, 2))

# These "asserts" are used for self-checking
assert count_divisible(10, 2) == 5
assert count_divisible(10, 3) == 3
assert count_divisible(10, 5) == 2
assert count_divisible(15, 4) == 3
assert count_divisible(20, 6) == 3
assert count_divisible(100, 10) == 10
assert count_divisible(200, 25) == 8
assert count_divisible(50, 7) == 7
assert count_divisible(60, 8) == 7
assert count_divisible(70, 9) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")