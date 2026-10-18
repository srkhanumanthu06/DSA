class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)
        start = 0

        # Process each group of k elements
        while start < n:
            left = start
            right = start + k - 1

            # If fewer than k elements remain, use the last index
            if right >= n:
                right = n - 1

            # Reverse the current group
            while left < right:
                # Swap the left and right elements
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp

                # Move towards the middle of the group
                left = left + 1
                right = right - 1

            # Move to the next group
            start = start + k
