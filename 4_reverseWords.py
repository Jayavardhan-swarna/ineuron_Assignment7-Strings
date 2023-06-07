def reverseWords(s):
    words = s.split()  # Split the string into words
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]  # Reverse the characters in the word
        reversed_words.append(reversed_word)

    reversed_sentence = " ".join(reversed_words)  # Join the reversed words with whitespace

    return reversed_sentence

s = "Let's take LeetCode contest"
reversed_string = reverseWords(s)
print(reversed_string)
