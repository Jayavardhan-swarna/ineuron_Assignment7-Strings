def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    char_map_s = {}
    char_map_t = {}

    for s_char, t_char in zip(s, t):
        if s_char not in char_map_s and t_char not in char_map_t:
            char_map_s[s_char] = t_char
            char_map_t[t_char] = s_char
        elif char_map_s.get(s_char) != t_char or char_map_t.get(t_char) != s_char:
            return False

    return True

s = "egg"
t = "add"
result = isIsomorphic(s, t)
print(result)
