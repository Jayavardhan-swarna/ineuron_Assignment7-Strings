def backspaceCompare(s, t):
    stack_s = []
    stack_t = []

    for char in s:
        if char != '#':
            stack_s.append(char)
        elif stack_s:
            stack_s.pop()

    for char in t:
        if char != '#':
            stack_t.append(char)
        elif stack_t:
            stack_t.pop()

    return stack_s == stack_t


s = "ab#c"
t = "ad#c"
result = backspaceCompare(s, t)
print(result)
