"""
Problem Description

Write a function that takes an integer and returns the number of 1 bits it has.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument contains integer A

Output Format
Return an integer as the answer

Example Input
Input1:
11

Example Output
Output1:
3
"""

"""Approach 1-And operation"""
# @param A : integer
# @return an integer
def numSetBits(self, A):
    count = 0
    while(A):
        A = A & A-1
        count += 1
    return count


"""Approach 2-Mod operation"""
# @param A : integer
# @return an integer
def numSetBits(A):
    count = 0
    while A > 0:
        temp = A % 2
        if temp == 1:
            count += 1
        A /= 2
    return count