def is_palindrome(string):
    string = "".join(char for char in string if char.isalnum())
    string = string.lower()
    return string == string[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
