class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        for x, f in count.items():
            if f == 1:
                return x
            

        