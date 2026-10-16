class Solution(object):
    def intersection(self, nums1, nums2):
        # Create a empty set
        h = {}

        # Store unique elements of nums1 in the set
        for i in nums1:
            if i not in h:
                h[i] = 1

        # Check which elements are common in nums2
        for i in nums2:
            if i in h and h[i] == 1:
                # Mark the common element as 2
                h[i] = 2

        # Return only the common elements
        return [i for i in h if h[i] == 2]
