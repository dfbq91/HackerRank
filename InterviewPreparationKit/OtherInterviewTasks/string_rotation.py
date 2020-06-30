#!/usr/bin/python3

# Using dictionaries
def string_rotation(str1, str2):
    str1, str2 = list(str1), list(str2)
    str1.sort()
    str2.sort()
    print(str1, str2)
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            return False
    return True


print(string_rotation('abcde', 'cdeab'))
