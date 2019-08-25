# -*- coding: utf-8 -*-
# Author  ：Rocklee
# Time  ：2019/8/25  15:27
n = int(input())
arr = list(map(int,input().split()))

tmp_arr = [0]*(n-1)
tmp_arr.insert(0,arr[0])

for i in range(1,n):
    tmp_arr[i] = max(tmp_arr[i-1]+arr[i],arr[i])
print(max(tmp_arr))
'''
7
-1 2 -1 3 1 -2 3
6
2 -1 -2 3 1 -2 
'''