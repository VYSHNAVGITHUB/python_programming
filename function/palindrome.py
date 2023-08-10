def palindrome(s):
    if s[::-1] == s:
        return "palindrome"
    else:
        return "not palindrome"
print(palindrome("malayalam"))
print(palindrome("abc"))