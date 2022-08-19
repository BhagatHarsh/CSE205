'''

'''


def revStr(s: str, l: int) -> str:
    if (l == 0):
        return s[l]
    return s[l] + revStr(s, l - 1)


s = input("Enter a string: ")
print('reversed string is: ' + revStr(s, len(s) - 1))
