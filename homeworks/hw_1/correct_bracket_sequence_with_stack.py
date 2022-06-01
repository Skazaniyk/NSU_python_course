def is_correct_brackets(str):
    stack = []
    for elements in str:
        if elements == "(":
            stack.append("(")
        if elements == ")":
            if stack:
                stack.pop(-1)
            else:
                return False
    if not stack:
        return True
    else:
        return False

print(is_correct_brackets(input()))
