"""
Problem Description

Given two binary strings, return their sum (also a binary string).
Example: ``` a = "100"

b = "11" Return a + b = "111".
"""

# @param A : string
# @param B : string
# @return a string
def addBinary(self, A, B):
    n1 = len(A)
    n2 = len(B)
    n = max(n1,n2)
    x = A.zfill(n)
    y = B.zfill(n)
    ans = ''
    carry = 0
    for i in range(n-1,-1,-1):
        temp = carry
        s1 = x[i]
        s2 = y[i]
        if s1 == '1':
            temp+=1
        if s2 == '1':
            temp+=1
        carry = 0 if temp<2 else 1
        ans = str(temp%2) + ans
    if carry:
        ans = str(carry)+ans
    return ans
