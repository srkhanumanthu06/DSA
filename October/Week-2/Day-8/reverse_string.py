class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        # Continue until both pointers meet
        while left < right:
            # Swap the characters
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left = left + 1
            right = right - 1
