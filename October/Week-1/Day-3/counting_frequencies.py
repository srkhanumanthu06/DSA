#Counting frequencies of array elements
class Solution:
    def countFreq(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        for num in freq:
            result.append([num, freq[num]])

        return result
