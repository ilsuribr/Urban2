from collections.abc import Iterable
from itertools import permutations

# def string_permutations(s: str) -> Iterable[str]:
#     # your code here
#     return sorted([''.join(x) for x in list((permutations(s)))])

def string_permutations(s: str) -> Iterable[str]:
    # your code here
    if len(s) == 1:
        return [s[0]]
    elif len(s) == 2:
        return sorted([s[0]+s[1]] + [s[1]+s[0]])
    elif len(s) == 3:
        return sorted([s[0]+x for x in string_permutations(s[1:])] +
                      [s[1]+x for x in string_permutations(s[0]+s[2])] +
                      [s[2]+x for x in string_permutations(s[:2])])
    elif len(s) == 4:
        return sorted(([s[0]+x for x in string_permutations(s[1:])] +
                [s[1]+x for x in string_permutations(s[0]+s[2:])] +
                [s[2]+x for x in string_permutations(s[:2]+s[3:])] +
                [s[3]+x for x in string_permutations(s[:3])]))


print("Example:")
print(list(string_permutations("aab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]
assert list(string_permutations('aab')) == ['aab', 'aab', 'aba', 'aba', 'baa', 'baa']

print("The mission is done! Click 'Check Solution' to earn rewards!")