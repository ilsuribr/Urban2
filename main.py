def translation(text: str) -> str:
    # your code here
    list_text = list(text)

    for i in range(len(list_text)):
        if list_text[i] not in "aeiouy" and list_text[i] not in ('', ' '):
            list_text[i + 1] = ''
        elif list_text[i] in "aeiouy" and list_text[i] != '':
            list_text[i + 1] = ''
            list_text[i + 2] = ''

    return ''.join(list_text)


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")

