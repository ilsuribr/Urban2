def all_variants(text):
    len_substr = 1
    while len_substr <= len(text):
        i_substr = 0
        while i_substr <= len(text) - len_substr:
            yield text[i_substr:i_substr + len_substr]
            i_substr += 1
        len_substr += 1


a = all_variants("abc")

for i in a:
    print(i)


