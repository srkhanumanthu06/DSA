# Leetcode 724. find pivot index
class Solution:
    def pivotIndex(self, nums):
        total = 0

        # Find the sum of all elements
        for i in range(len(nums)):
            total = total + nums[i]

        left_sum = 0

        # Check each index
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            # Check if left sum and right sum are equal
            if left_sum == right_sum:
                return i

            # Add the current element to the left sum
            left_sum = left_sum + nums[i]

        return -1
