def addStrings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        # Add digits along with the carry
        digit_sum = digit1 + digit2 + carry

        # Compute new carry and digit
        carry = digit_sum // 10
        digit = digit_sum % 10

        # Append the new digit to the result
        result = str(digit) + result

        # Move the pointers
        i -= 1
        j -= 1

    # Add the remaining carry if any
    if carry > 0:
        result = str(carry) + result

    return result

num1 = "11"
num2 = "123"
result = addStrings(num1, num2)
print(result)
