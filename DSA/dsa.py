# Valid anagram

def valid_anagram(a: str, b: str):
    return sorted(a) == sorted(b)

print(valid_anagram("aab", "baa"))
print(valid_anagram("papa", "appa"))
print(valid_anagram("aab", "bba"))