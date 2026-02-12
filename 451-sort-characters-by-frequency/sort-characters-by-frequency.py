class Solution:
    from collections import Counter
    def frequencySort(self, s: str) -> str:
        ans = []
        count = Counter(s)
        n = list(count.keys())
        n.sort(key=lambda x: -count[x])
        #print(n)
        for x in n:
            freq = count[x]
            for _ in range(freq):
                ans.append(x)
        return ''.join(ans)

