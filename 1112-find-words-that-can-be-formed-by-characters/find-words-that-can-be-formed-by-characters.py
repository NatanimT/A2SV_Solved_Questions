class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chr_freq = {}
        summ = 0
        for i in chars:
            chr_freq[i] = chr_freq.get(i, 0) + 1
        for j in words:
            freq = Counter(j)
            for k in j:
                if k not in chr_freq or freq[k] > chr_freq.get(k, 0):
                    break
            else:
                summ += len(j)
        return summ


        