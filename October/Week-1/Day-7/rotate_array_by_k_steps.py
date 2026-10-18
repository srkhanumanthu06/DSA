class Solution:
    def rotateclockwise(self, arr, k):
        
        n = len(arr)

        if n == 0:
            return

        k = k % n

        # Reverse the entire array
        left = 0
        right = n - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1

        # Reverse the first k elements
        left = 0
        right = k - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1

        # Reverse the remaining elements
        left = k
        right = n - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1
