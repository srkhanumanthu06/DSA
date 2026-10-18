class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n

        # Reverse the first d elements
        left = 0
        right = d - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1

        # Reverse the remaining elements
        left = d
        right = n - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1

        # Reverse the entire array
        left = 0
        right = n - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1
