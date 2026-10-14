Day 3 · Oct 3 Sat
Topic: Hashmap counting
DON'T REACH FOR: Counter, Counter.most_common(). Use a plain dict with manual increment.
1. Majority Element
2. First Non-Repeating Element in Array
3. Count Frequencies of Array Elements

Question 1: Majority element

Problem : Given an array arr[] of size n, find the element that appears more than ⌊n/2⌋ times. If no such element exists, return -1.

Examples:
Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1
Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3, it is the majority element.

Input: arr[] = [7]
Output: 7
Explanation: Element 7 appears once. Since ⌊1/2⌋ = 0, and 1 > 0, it is the majority element.

Input: arr[] = [2, 13]
Output: -1
Explanation: No element appears more than ⌊2/2⌋ = 1 time, so there is no majority element.

------------------------------------------------------------------------------------------------------

Question 2: First non repeating element in array

Problem : Given an array arr[] of integers of size n, find the first non-repeating element in this array.  if no such element exists return 0.

Examples:

Input: arr[] = [-1, 2, -1, 3, 2]
Output: 3
Explanation: -1 and 2 are repeating whereas 3 is the only number occuring once. Hence, the output is 3. 

Input: arr[] = [1, 1, 1]
Output: 0
Explanation: There is not present any non-repeating element so answer should be 0.

---------------------------------------------------------------------------------------------------------

Question 3: Counting frequencies of array elements

Problem : Given an array arr[] of non-negative integers which may contain duplicate elements. Return the frequency of each distinct element present in the array.

Examples: 

Input:  arr[] = [10, 20, 10, 5, 20]
Output: [[5, 1], [10, 2], [20, 2]]
Explanation: Here 5 occurs once, 10 occurs 2 times and 20 occurs 2 times.

Input: arr[] = [10, 20, 20]
Output: [[10, 1], [20, 2]] 
Explanation: Here 10 occurs 1 time, 20 occurs 2 times.

----------------------------------------------------------------------------------------------------------
