def is_palindrome(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        print(s[0], "is not equal to ",s[-1])
        return False
    else:
        return is_palindrome(s[1:-1])

print(is_palindrome("level"))

def recursive_exponentiation(x,y):
    if y == 1:
        return x
    else:
        return (x * recursive_exponentiation(x, y-1))