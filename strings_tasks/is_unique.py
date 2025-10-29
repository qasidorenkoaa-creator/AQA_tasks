def is_unique(string):
    seen_chars = set()

    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)

    return True


print(is_unique("abcdef"))
print(is_unique("hello"))
