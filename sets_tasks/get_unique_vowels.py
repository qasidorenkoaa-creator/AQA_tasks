def get_unique_vowels(string):
    list_string = list(string.lower())
    list_string.remove(" ")
    return set(list_string) & set(vowel_letters)


vowel_letters = ["a", "e", "i", "o", "u"]
print(get_unique_vowels("Hello World"))


# второй способ (порядок не сохраняется!)
def get_unique_vowels(string):
    return {char for char in string.lower() if char in vowel_letters}


vowel_letters = "aeiou"
print(get_unique_vowels("Hello World"))


# третий способ (порядок сохраняется!)
def get_unique_vowels_ordered(string):
    vowels = "aeiou"
    new_list = []
    for char in string.lower():
        if char in vowels and char not in new_list:
            new_list.append(char)
    return new_list


print(get_unique_vowels_ordered("Hello World"))
