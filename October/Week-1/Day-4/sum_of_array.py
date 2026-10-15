#sum of arrays
class Solution:
    def arraySum(self, arr):
        total = 0

        for num in arr:
            total = total + num

        return total
