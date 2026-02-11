class Solution:
    def findValidPair(self, s: str) -> str:
        count = {}
        ans = ""
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
        # item = list(count.items())
        for i in range(len(s)-1):
            key1, key2 = s[i], s[i + 1]
            val1, val2 = count[key1], count[key2]
            if key1 != key2 and int(key1) == val1 and int(key2) == val2:
                ans += key1 + key2
                return ans
                
        return ans

        