def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

string = "Hello World"
result = count_vowels(string)
print(f"Количество гласных в строке '{string}': {result}")

# 2 способ
def count_vowels(string):
    return sum(1 for char in string.lower() if char in "aeiou")

string = "Hello World"
result = count_vowels(string)
print(f"Количество гласных в строке '{string}': {result}")