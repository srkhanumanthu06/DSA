# 303. range sum query - immutable
class NumArray:

    def __init__(self, nums):
        self.prefix = []  # Store the prefix sums
        total = 0

        # Calculate the running sum
        for i in range(len(nums)):
            total = total + nums[i]
            self.prefix.append(total)

    def sumRange(self, left, right):
        # If left is 0, return the prefix sum directly
        if left == 0:
            return self.prefix[right]

        # Subtract the sum before left from the sum up to right
        return self.prefix[right] - self.prefix[left - 1]
