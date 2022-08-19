'''

'''


def revStr(s: str, l: int) -> str:
    if (l == 0):
        return s[l]
    return s[l] + revStr(s, l - 1)


s = input("Enter a string: ")
if (s == revStr(s, len(s) - 1)):
    print('String is Palindrome')
else:
    print('String is Not plaindrome')
