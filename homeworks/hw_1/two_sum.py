def two_sum(array, n):
    dictionary = dict()
    for i, item in enumerate(array):
        if n - item in dictionary:
            print([dictionary[n - item], i])
        else:
            dictionary[item] = i


two_sum([2,7,11,15], 9)
