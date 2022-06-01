import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--project_dir")
args = parser.parse_args()


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


path = input()
path_gitignore = find('.gitignore', path)
with open(path_gitignore) as gitignore:
    lines = list(map(lambda x: x.replace('\n', ''), gitignore.readlines()))

print(lines)
pattern_1 = "\*\.[a-zA-Z0-9]"
print("Ignored files:")
for line in lines:
    if (re.search(pattern_1, line)):
        pattern_2 = "[a-zA-Z0-9]" + line
        for element in os.listdir(path.split("/")[-1]):
            if (re.search(pattern_2, element)):
                print(os.path.abspath(element) + " ignored by expression " + line)
    else:
        if (os.path.exists(os.path.join(path, line))):
            print(path.split("/")[-1] + "\\" + line + " ignored by expression " + line)
