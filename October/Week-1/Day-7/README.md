Day 7 · Oct 7 Wed 

Topic: Array rotation 

DON'T REACH FOR: nums[k:] + nums[:k] slice trick. Rotate in-place with three reverses.

3 PROBLEMS

● 1. Rotate Array 

● 2. Rotate Array by K Steps (in-place) 

● 3. Reverse Array in Groups

------------------------------------------------------------------

QUESTION 1: Rotate array

Problem: Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes [3, 4, 5, 1, 2].
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes [8, 10, 12, 14, 16, 18, 20, 2, 4, 6].
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get [3, 9, 1, 7] as resultant array.

----------------------------------------------------------

QUESTION 2: Rotae array by k steps

Problem: Given an array of arr[] of size n, the task is to rotate the array elements to the left by d positions.

Examples:

Input: arr[] = [1, 2, 3, 4, 5, 6], d = 2
Output: [3, 4, 5, 6, 1, 2]
Explanation: After first left rotation, arr[] becomes [2, 3, 4, 5, 6, 1] and after the second rotation, arr[] becomes [3, 4, 5, 6, 1, 2]

Input: arr[] = [1, 2, 3], d = 4
Output: [2, 3, 1]
Explanation: The array is rotated as follows:

After first left rotation, arr[] = [2, 3, 1]
After second left rotation, arr[] = [3, 1, 2]
After third left rotation, arr[] = [1, 2, 3]
After fourth left rotation, arr[] = [2, 3, 1]

-------------------------------------------------------------

QUESTION 3: Reverse array in groups

Problem: Given an integer array arr[] and an integer k, reverse every consecutive group of k elements. If fewer than k elements remain at the end, reverse all of them.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4, 5.
Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]
Explnation: Since k is greater than the number of remaining elements, the entire array is reversed.


