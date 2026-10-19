class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = "aeiouAEIOU"
        while left < right:
            if s[left] not in vowels:
                left = left + 1
            elif s[right] not in vowels:
                right = right - 1
            else:
                #swap the vowels
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
              
                #pointers toward the center
                left = left + 1
                right = right - 1
              
        #convert the charcater list back into a string
        return "".join(s)
