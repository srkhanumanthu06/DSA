class Solution(object):
    def findDisappearedNumbers(self, nums):
        # find the length of the array
        n = len(nums)

        # create an empty list to place the missing numbers
        result = []

        # check numbers from 1 to n
        for i in range(1, n + 1):
            # if the number is not in the array then add it to result
            if i not in nums:
                result = result + [i]

        # return the missing numbers
        return result
