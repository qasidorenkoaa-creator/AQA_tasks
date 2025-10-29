def group_by_first_letter(strings):
    fruit_dict = {first_letter: [fruit_name for fruit_name in strings if fruit_name.startswith(first_letter)]
                  for first_letter in [fruit_name[0] for fruit_name in strings]}
    return fruit_dict


strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))


# второй способ
def group_by_first_letter(strings):
    fruit_dict = {}
    for fruit_name in strings:
        first_letter = fruit_name[0]
        if first_letter not in fruit_dict:
            fruit_dict[first_letter] = []
        fruit_dict[first_letter].append(fruit_name)
    return fruit_dict


strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
