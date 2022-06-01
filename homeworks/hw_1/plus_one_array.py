def plus_one(array):
    number_in_mind = 1
    for elements in range(len(array) - 1, -1, -1):
        array[elements] += number_in_mind
        if(array[elements] == 10):
            array[elements] = 0
            number_in_mind = 1
        else:
            number_in_mind = 0
    if number_in_mind:
        array.insert(0, 1)
    return array

print(plus_one([9,9,9]))
