#Leetcode problem 53: Maximum subarray
class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        largest = nums[0]

        for i in range(1, len(nums)):
            if current + nums[i] > nums[i]:
                current = current + nums[i]
            else:
                current = nums[i]

            if current > largest:
                largest = current

        return largest
