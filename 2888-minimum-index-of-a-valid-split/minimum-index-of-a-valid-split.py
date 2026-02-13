class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        count = Counter(nums)
        n = len(nums)

        dominant = -1
        for num in count:
            if count[num] > n // 2:
                dominant = num
                break
        if dominant == -1:
            return -1

        left_count = 0

        for i in range(n):
            if nums[i] == dominant:
                left_count += 1

            left_size = i + 1
            right_size = n - i - 1
            right_count = count[dominant] - left_count

            if (left_count > left_size // 2 and
                right_count > right_size // 2):
                return i

        return -1






        