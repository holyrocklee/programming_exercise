# -*- coding: utf-8 -*-
# Author  ：Rocklee
# Time  ：2019/8/25  15:27
#题目描述：一个数组有 N 个元素，求连续子数组的最大和。 例如：[-1,2,1]，和最大的连续子数组为[2,1]，其和为 3
# 输入描述:
# 输入为两行。
# 第一行一个整数n(1 <= n <= 100000)，表示一共有n个元素
# 第二行为n个数，即每个元素,每个整数都在32位int范围内。以空格分隔。
# 输出描述:所有连续子数组中和最大的值
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