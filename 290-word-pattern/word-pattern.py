class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # "abba"  ["dog", "cat" "cat" "fish"
        n = s.split()
        if len(n) != len(pattern):
            return False
        hasmap1 = {}
        hasmap2 ={}
        for char, word in zip(pattern, n):
            if char in hasmap1 and hasmap1[char] != word:
                return False
            if word in hasmap2 and hasmap2[word] != char:
                return False
            hasmap1[char] = word
            hasmap2[word] = char
        return True
