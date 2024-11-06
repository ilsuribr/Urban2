def longest_substr(s: str) -> int:
    # your code here
    count = 0
    for i in range(len(s)):
        set_s = set()
        for j in range(i, len(s)):
            if s[j] not in set_s:
                set_s.add(s[j])
            else:
                break
        if count < len(set_s):
            count = len(set_s)

    return count


print("Example:")
print(longest_substr("pwwkew"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")