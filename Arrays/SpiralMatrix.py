"""
Problem Description

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Problem Constraints
1 <= A <= 1000

Input Format
First and only argument is integer A

Output Format
Return a 2-D matrix which consists of the elements in spiral order.

Example Input
Input 1:
1

Input 2:
2

Example Output
Output 1:
[ [1] ]

Output 2:
[ [1, 2], [4, 3] ]
"""

def generateMatrix(self, A):
    l = t = 0
    b = r = A-1
    arr = []
    for i in range(A):
       # arr.append([])
        arr.append([0]*A)
    x=1
   # print(arr)
    while l<=r and t<=b:
        for i in range(l,r+1):
            arr[t][i] = x
            x+=1
        t+=1
        for i in range(t,b+1):
            arr[i][r] = x
            x+=1
        r-=1
        for i in range(r,l-1,-1):
            arr[b][i]=x
            x+=1
        b-=1
        for i in range(b,t-1,-1):
            arr[i][l]=x
            x+=1
        l+=1
    return arr
