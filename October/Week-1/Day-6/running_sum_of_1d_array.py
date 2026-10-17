# leetcode 1480. Running sum of 1d array
class Solution:
    def runningSum(self, nums):
        result = []  # Store the running sums
        total = 0    # Keep track of the sum

        # Go through each element in the array
        for i in range(len(nums)):
            total = total + nums[i]  # Add current element to total
            result.append(total)     # Add total to the result list

        return result  # Return the running sum array
