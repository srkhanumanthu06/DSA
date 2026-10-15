# maximum consecutive ones in a binary array
class Solution:
    def maxConsecBits(self, arr):
        if len(arr) == 0:
            return 0

        count = 1
        maximum = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1

            if count > maximum:
                maximum = count

        return maximum
