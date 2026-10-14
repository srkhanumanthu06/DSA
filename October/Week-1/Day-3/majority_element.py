class Solution:
    def majorityElement(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] > len(arr) // 2:
                return num

        return -1
