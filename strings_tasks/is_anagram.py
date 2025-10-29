def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    return sorted(string1) == sorted(string2)


print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
