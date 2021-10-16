"""
Problem Description

Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

Return the count modulo 10^9 + 7.

Problem Constraints
1 <= A <= 10^9

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the ( Total number of set bits in the binary representation of all the numbers from 1 to A )modulo 109 + 7.

Example Input
Input 1:
A = 3

Input 2:
A = 1

Example Output
Output 1:
4

Output 2:
1
"""

# @param A : integer
# @return an integer
def solve(A):
    def sumSetBits(n):
        if n == 1 or n == 0:
            return n
        import math
        mod = pow(10,9)+7
        ans = 0
        x = int(math.log(n, 2))
        a = pow(2, x)
        # f(n) = f(a-1)+f(n-a)+(n-a+1) -> TC: O(n)
        # f(n) = x*(a/2) + f(n-a) + (n-a+1) -> TC: O(lg n)
        ans += x*(a // 2) + sumSetBits(n-a) + (n-a+1)
        ans %= mod
        return ans
    return sumSetBits(A)
