from collections import deque


def is_correct_brackets(str):
    my_deque = deque()
    for bracket in str:
        if bracket == '(':
            my_deque.append('(')
        elif bracket == ')' and len(my_deque) == 0:
            return False
        else:
            my_deque.pop()
    if len(my_deque) == 0:
        return True
    return False


print(is_correct_brackets(input()))
