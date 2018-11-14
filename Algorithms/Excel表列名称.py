# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:59:59 2018

@author: xiaohong
"""


'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"
'''




'''
我的 0.29
'''

def convertToTitle(n):
        """
        :type n: int
        :rtype: str
        """
        tmp = []
        char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        quotient = n
        while quotient > 0:
            res = (quotient-1) % 26 + 1
            quotient = (quotient-1) // 26
            tmp.append(res)            
        excelName = ''    
        while tmp != []:
            excelName =  excelName + char[tmp.pop()-1]
        return excelName
    
    
  
convertToTitle(702)
convertToTitle(52)
convertToTitle(53)

convertToTitle(25)
convertToTitle(26)
convertToTitle(1)

'''
第二次做：时间复杂度O(n) 空间复杂度O(1)
思路：递归，递归出口是s的长度只有１位，然后就是self.ans加上最后以为对应的分数
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                 'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        self.ans = 0
        self.helper(s)
        return self.ans
        
    def helper(self,s):
        if len(s)==1:
            self.ans += self.alpha[s[0]]
            return
        elif len(s)>1:
            self.ans += self.alpha[s[0]]*26**(len(s)-1)
            self.helper(s[1:])

'''
最简洁的代码
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s:
            res = (ord(i)-64) + res * 26
        return res