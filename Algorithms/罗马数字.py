# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:02:05 2018

@author: xiaohong
"""



'''
罗马数字
'''

'''
我的代码
'''
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        roma = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        for i in range(len(s)):
            if i < len(s)-1:
                if s[i] == 'I':
                    if s[i+1] == 'V' or s[i+1] == 'X':
                        num = num - 1
                    else:
                        num = num + 1
                elif s[i] == 'X':
                    if s[i+1] == 'L' or s[i+1] == 'C':
                        num = num - 10
                    else:
                        num = num + 10
                elif s[i] == 'C':
                    if s[i+1] == 'D' or s[i+1] == 'M':
                        num = num - 100
                    else:
                        num = num + 100
                else:
                    num = num + roma[s[i]]
            else:
                num = num + roma[s[i]]
        return num
    


'''
LeetCode@agav的代码 
'''    
def romanToInt(s):
    d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    res, p = 0, 'I'
    for c in s[::-1]:
        res, p = res - d[c] if d[c] < d[p] else res + d[c], c
    return 


