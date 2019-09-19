# -*- coding: utf-8 -*-
# Author  ：Rocklee
# Time  ：2019/8/25  18:24

while True:
    try:
        s = input().strip()

        def solve(eq, var='X'):
            eqi = eq.replace('=', '-(') + ')'
            print(eqi)
            c = eval(eqi, {var: 1j})
            print(c)
            return -c.real / c.imag if c.imag else -1

        print(int(solve(s)))
    except:
        break
'''
2*X=6
'''