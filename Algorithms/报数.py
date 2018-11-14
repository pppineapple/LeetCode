# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 07:55:11 2018

@author: xiaohong
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """        
        if n == 1:
            return '1'
        
        def next(item):
            if item == '1':
                return '11'
            if item == '11':
                return '21'
            if item  == '21':
                return '1211'
            i = 0
            j = 0
            num = []
            num_count = []
            count = 0            
            while j < len(item):
                if item[i] == item[j]:
                    count += 1
                    j += 1
                else:
                    num.append(item[i])
                    num_count.append(count)
                    count = 0
                    i = j
                    print i,j,count
            num.append(item[i])
            num_count.append(count)                    
            
            output = ''
            for i in range(len(num)):
                output = output + str(num_count[i]) + num[i]
            return output
        
        output = '1'
        for i in range(2, n+1):
            output = next(output)
        return output
    
    
'''
第二次做：　时间复杂度O(n^2) 空间复杂度(n)
思路：字符串处理，编写辅助函数递归产生字符串 
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        opt = [''] * n
        opt[0] = '1'
        for i in range(1,n):
            opt[i] = self.generate(opt[i-1])
        return opt[-1]
        
    def generate(self, x):
        i = 0
        output = ''
        while i < len(x):
            count = 1
            while i < len(x)-1 and x[i] == x[i+1]:
                count += 1
                i += 1            
            output += str(count) + x[i]
            i += 1
        return output