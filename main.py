def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    if first == second or word.find(first) == -1 or word.find(second) == -1:
        return False
    else:
        if word.find(first + second) == -1:
            return False
        else:
            if word.find(first) != word.find(second) - 1:
                return False
            else:
                return True


print("Example:")
print(goes_after("transport", "r", "t"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")