s = "greetings, friends."

if s[0].islower():
    s = s[0].upper() + s[1:]
if s[-1] != '.':
    s = s + '.'

print(s)