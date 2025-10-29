def char_frequency(string):
    letters = list(string)
    new_dict = {letter: string.count(letter) for letter in letters}
    return new_dict


print(char_frequency("hello"))


# второй способ
def char_frequency(string):
    new_dict = {}
    for char in string:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict


print(char_frequency("hello"))
