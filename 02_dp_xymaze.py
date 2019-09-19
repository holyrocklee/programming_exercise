# -*- coding: utf-8 -*-
# Author  ：Rocklee
# Time  ：2019/8/25  16:03
# 题目描述：X*Y的网格迷宫
# 有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。
# 请设计一个算法，计算小团有多少种走法。给定两个正整数int x,int y，请返回小团的走法数目。

# 思路： 动态规划，使用递推方程d[i][j] = d[i-1][j] + d[i][j-1],即考虑从右下角[i][j]走回左上角[1][1]
# 因为可能从两个方向走到同一个点，所以从上到下为一种走法，从左到右是另一种走法
# 注意题目给的是x*y方格，所以是(x+1)*(y+1)个点
x,y = list(map(int,input().split()))
d = [[0]*(y+2) for i in range(x+2)]
# print(d)
for i in range(1,x+2):
    for j in range(1,y+2):
        if i==1 and j==1:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j]+d[i][j-1]
print(d)
print(d[-1][-1])