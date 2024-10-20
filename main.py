from itertools import zip_longest

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    # your code here
    zipped = list(zip_longest(str1, str2, fillvalue=None))
    count = sum(list(map(lambda x: 1 if x[0] != x[1] else 0, zipped)))
    if count <= threshold:
        return True
    else:
        return False


print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
