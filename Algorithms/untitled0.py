#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:33:44 2018

@author: pineapple
"""
'''
你需要找到由两个 n 位数的乘积组成的最大回文数。

由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。

示例:

输入: 2

输出: 987

解释: 99 x 91 = 9009, 9009 % 1337 = 987

说明:

n 的取值范围为 [1,8]。
'''

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def ispalindrome(num):
            if len(str(num)) % 2 != 0:
                return False
            half = len(str(num))//2
            return str(num)[:half] == str(num)[::-1][:half]
        
        '''
        需要检查此回文数是否可以由两个数相乘得到（即，使此数依次除以某n位数，看余数是否为0）。
        若进行除法运算后，商大于n位数的最大值，则跳出此次循环，
        '''
        def istwonumbermatmul(num, max_n):
            while num % max_n != 0:
                rem = num // max_n
                max_n -= 1
                if rem > max_n:
                    break
            if num % max_n == 0:
                return True
            else:
                return False     
              
        if n == 1:
            return 9 % 1337
        else:
            min_n = 10**(n-1)
            max_n = 10**n-1
        
        min_result = min_n * min_n
        max_result = max_n * max_n
        
        for i in range(max_result, min_result-1, -1):
            if ispalindrome(i) and istwonumbermatmul(i, max_n):
                return i % 1337

n = 2
s = Solution()
s.largestPalindrome(4)
        
          
