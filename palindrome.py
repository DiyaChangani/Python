s = "radar"

def p(s):
    if len(s)==1:
        return s + "is a palindrome"
    else:
        if s == s[::-1]:
            return s + " is a palindrome"
        else:
            return s + "is not a palindrome"


print(p(s))