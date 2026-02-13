class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # bbcbaa aabbbc
        # aacabb aaabbc a:3 
        # bbcbaa aabbbc b:3
        count1 = Counter(word1)
        # print(count1)
        count2 = Counter(word2)
        # if sorted[word1] == sorted[word2]:
        #     return True
        # elif 
        if len(word1) != len(word2):
            return False
        if count1.keys() != count2.keys():
            return False
        return sorted(count1.values()) == sorted(count2.values())