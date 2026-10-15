Day 4 
Topic: Running state in one pass
DON'T REACH FOR: itertools.accumulate(), max() across slices.
3 PROBLEMS (all required)
● 1. Running Sum of 1d Array
● 2. Max Consecutive Ones
● 3. Best Time to Buy and Sell Stock

Question 1 : running sum of 1d array

Problem: Given an integer array arr[], return the sum of all elements of arr.

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.
---------------------------------------------------------------------------------

Question 2 : Max consecutive ones

Problem: Given a binary array arr[] consisting of only 0s and 1s, find the length of the longest contiguous sequence of either 1s or 0s in the array.

Examples : 

Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
Output: 4
Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.

Input: arr[] = [0, 0, 1, 0, 1, 0]
Output: 2
Explanation: The maximum number of consecutive 0’s in the array is 2 from index 0-1.

Input: arr[] = [0, 0, 0, 0]
Output: 4
Explanation: The maximum number of consecutive 0’s in the array is 4.
-------------------------------------------------------------------------------------

Question 3 : Best time to buy and sell stocks

Problem: Given an array prices[] of non-negative integers, representing the prices of the stocks on different days, return the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: Buy for price 1 and sell for price 9. 

Input: prices[] = [7, 6, 4, 3, 1]
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = [1, 3, 6, 9, 11]
Output: 10
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]
-----------------------------------------------------------------------------------------
