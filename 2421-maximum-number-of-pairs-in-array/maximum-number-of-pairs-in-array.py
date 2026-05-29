class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        pair = 0
        s =0
        for i, val in cnt.items():
            pair += val // 2
            s += val % 2
        return [pair, s]

            