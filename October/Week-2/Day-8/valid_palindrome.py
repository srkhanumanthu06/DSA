class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip special characters from the left
            if not s[left].isalnum():
                left = left + 1

            # Skip special characters from the right
            elif not s[right].isalnum():
                right = right - 1

            # compare both characters in lowercase
            elif s[left].lower() != s[right].lower():
                return False

            else:
                # to move left pointer forward
                left = left + 1

                # to move right pointer backward
                right = right - 1

        # if all characters match, it is a palindrome
        return True
