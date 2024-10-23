def longest_prefix(arr: list[str]) -> str:
    # your code here
    pref = []

    for i in range(len(min(arr, key=len))):
        set_pref = set()
        for k in range(len(arr)):
            set_pref.add(arr[k][i])
        pref.append(set_pref)

    prefix = ''
    for i in range(len(pref)):
        if len(pref[i]) == 1:
            prefix += pref[i].pop()
        else:
            break

    return prefix


print("Example:")
print(repr(longest_prefix(["flower", "flow", "flight"])))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")


arr = ['aa', 'ba']

pref = []

for i in range(len(min(arr, key=len))):
    set_pref = set()
    for k in range(len(arr)):
        set_pref.add(arr[k][i])
    pref.append(set_pref)

prefix = ''

print(pref)

for i in range(len(pref)):
    if len(pref[i]) == 1:
        prefix += pref[i].pop()
    else:
        break

print(prefix)





