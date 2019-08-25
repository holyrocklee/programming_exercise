# -*- coding: utf-8 -*-
# Author  ：Rocklee
# Time  ：2019/8/25  12:24

#如何求数字的组合
# 题目描述：
# 用l 、2 、2 、3 、4 、5 这六个数字，写一个main 函数，打印出所有不同的排列，例如：
# 512234 、412345 等，要求：“4 ”不能在第三位，“ 3 ”与“ 5 ”不能相连。
import itertools
s =list(map(int,input().split()))
n = len(s)
arr = list(itertools.permutations(s))
# print(arr)
tmp = []
for i in range(len(arr)):
    count = 0
    for j in range(0,n-1):
        if (j==2 and arr[i][j]==4) or (arr[i][j]==3 and arr[i][j+1]==5) or (arr[i][j]==5 and arr[i][j+1]==3):
            count+=1
        else:
            pass
    if count==0:
        tmp.append(arr[i])
print(tmp)
print((5,1,2,2,3,4) in tmp)  #True
print((2,1,2,3,4,5) in tmp)  #True

'''
1 2 2 3 4 5
'''