class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = collections.deque() 
        dec = collections.deque() 
        ans = 0
        left = 0
        for right, val in enumerate(nums):
            while inc and val < inc[-1]:
                inc.pop()
            inc.append(val)
            while dec and val > dec[-1]:
                dec.pop()
            dec.append(val)
            while abs(dec[0] - inc[0]) > limit:
                if dec[0] == nums[left]:
                    dec.popleft()
                if inc[0] == nums[left]:
                    inc.popleft()
                left += 1
 
            ans = max (ans, right - left + 1)
        return ans


