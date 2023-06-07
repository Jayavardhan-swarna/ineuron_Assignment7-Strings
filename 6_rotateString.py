def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    concatenated = s + s
    if goal in concatenated:
        return True

    return False

s = "abcde"
goal = "cdeab"
result = rotateString(s, goal)
print(result)
