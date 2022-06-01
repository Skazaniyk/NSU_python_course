from collections import defaultdict


def invert(dictionary):
    invert_dict = defaultdict(set)
    for key, value in dictionary.items():
        invert_dict[value].add(key)

    invert_dict = sorted(invert_dict.items(), key=lambda x: x[0])
    return dict(invert_dict)


print(invert({"a": 42, "b": 42, "c": 24}))
