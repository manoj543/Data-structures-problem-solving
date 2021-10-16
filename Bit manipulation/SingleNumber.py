"""
Problem Description

Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?


Problem Constraints
2 <= A <= 5106

0 <= A <= INTMAX

Input Format
First and only argument of input contains an integer array A.

Output Format
Return a single integer.

Example Input
Input 1:

A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

Input 2:
A = [0, 0, 0, 1]

Example Output
Output 1:
4

Output 2:
1
"""


# @param A : tuple of integers
# @return an integer
def singleNumber(A):
    ones = 0
    twos = 0
    for elem in A:
        twos = twos | (ones & elem)
        ones = ones ^ elem
        not_threes = ~(ones & twos)
        ones = ones & not_threes
        twos = twos & not_threes
    return ones
