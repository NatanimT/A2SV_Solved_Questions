class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = sum(num for num in nums if num % 2 == 0)
        result = []

        for value, index in queries:
            if nums[index] % 2 == 0:
                sum_even -= nums[index]

            nums[index] += value

            if nums[index] % 2 == 0:
                sum_even += nums[index]

            result.append(sum_even)

        return result