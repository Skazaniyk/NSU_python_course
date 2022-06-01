def number_of_unique_characters(string):
    dictionary = dict()
    for character in string:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary

print(number_of_unique_characters(input()))
