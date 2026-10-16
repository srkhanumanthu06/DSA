class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        # Calculate the sum of numbers from 0 to n
        total = n * (n + 1) // 2
        # Calculate the sum of elements in the array
        arr_sum = sum(nums)
        # Find the missing number
        return total - arr_sum
