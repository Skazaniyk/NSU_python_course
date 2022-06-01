from string import punctuation
from collections import Counter

with open("zen_python", "r") as file:
    counter = Counter()
    for lines in file.readlines():
        for p in punctuation:
            lines = lines.replace(p, " ")
        lines = lines.replace("\n", " ")
        lines = lines.lower()
        if not lines:
            continue
        lines = lines.split()
        counter.update(lines)
print(*counter.most_common(10))
