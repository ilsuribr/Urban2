def middle(text: str) -> str:
    # replace this for solution
    res = ""
    if len(text) % 2 == 0:
        res = text[(len(text) // 2) - 1] + text[(len(text) // 2)]
    else:
        res = text[(len(text) // 2)]

    return res


print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")

