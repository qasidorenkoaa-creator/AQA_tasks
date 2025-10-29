def longest_word(string):
    words = string.split()
    max_long_word = max(words, key=len)
    return max_long_word


print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))
