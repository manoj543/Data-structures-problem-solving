"""
Problem Description

Reverse the bits of an 32 bit unsigned integer A.

Problem Constraints
0 <= A <= 232

Input Format
First and only argument of input contains an integer A.

Output Format
Return a single unsigned integer denoting the decimal value of reversed bits.

Example Input
Input 1:
0

Input 2:
3

Example Output
Output 1:
0

Output 2:
3221225472
"""

# @param A : unsigned integer
# @return an unsigned integer
def reverse(A):
    b1 = bin(A).replace('0b', '')
    b1 = b1.zfill(32)  # Zero filling
    b2 = ''
    total_bits = len(b1)
    j = total_bits - 1
    while(j>=0):
        b2 += b1[j]
        j -= 1
    return int(b2,2)
