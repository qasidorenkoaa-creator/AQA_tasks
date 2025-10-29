def remove_duplicates(string):
    unique_chars = set()
    output_chars = []

    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            output_chars.append(char)

    return "".join(output_chars)


print(remove_duplicates("programming"))
