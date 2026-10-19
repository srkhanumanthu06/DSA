class Solution(object):
    def isPalindrome(self, s):
        # Start left pointer at the beginning
        left = 0

        # Start right pointer at the end
        right = len(s) - 1

        # Continue until both pointers meet
        while left < right:

            # Skip special characters from the left
            if not s[left].isalnum():
                left = left + 1

            # Skip special characters from the right
            elif not s[right].isalnum():
                right = right - 1

            # Compare both characters in lowercase
            elif s[left].lower() != s[right].lower():
                return False

            else:
                # Move left pointer forward
                left = left + 1

                # Move right pointer backward
                right = right - 1

        # If all characters match, it is a palindrome
        return True
