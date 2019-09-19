# -*- coding: utf-8 -*-
# Author  ：Rocklee
# Time  ：2019/8/26  9:59
#方法1：此解法内存超出限制
import itertools
n = int(input())
s = 'ABC'
no_repeat = [] #表示含有连续完整的'ABC'、'ACB'等三个字符的
if n<3:
    print(len(list(itertools.product(s,repeat=n))))
else:
    # list(itertools.product(s,repeat=n))可以把三种元素的排列组合，包括有重复元素和没有重复元素的情况
    tmp = []
    for i in list(itertools.product(s,repeat=n)):
        tmp.append(''.join(i))
    # print(tmp)
    for j in tmp:
        if ('ABC' in j) or ('ACB' in j)or('BCA' in j)or('BAC' in j)or('CAB' in j)or('CBA' in j):
            no_repeat.append(j)
    print(len(list(itertools.product(s,repeat=n)))-len(no_repeat))
'''
2:9
3:21
4:51
5:123
'''
#方法2：动态规划
'''
n = int(input())
dp = [0]*31
dp[2] = 21
dp[1] = 9
for i in range(3, n):
    dp[i] = 2*dp[i-1]+dp[i-2]
print(dp[n-1])
'''
