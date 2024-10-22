def count_occurrences(main_str: str, sub_str: str) -> int:
    # your code here
    i = 0
    count = 0
    while i <= len(main_str) and (len(sub_str) != 0):
        k = main_str.lower().find(sub_str.lower(), i)
        if k != -1:
            count += 1
            i = k + 1
        else:
            break
    return count


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")