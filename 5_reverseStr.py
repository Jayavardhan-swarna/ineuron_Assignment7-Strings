def reverseStr(s, k):
    chars = list(s)  # Convert the string into a list of characters

    for i in range(0, len(chars), 2*k):
        # Reverse the first k characters in the chunk
        chars[i:i+k] = chars[i:i+k][::-1]

    return ''.join(chars)  # Join the characters back into a string

s = "abcdefg"
k = 2
reversed_string = reverseStr(s, k)
print(reversed_string)
