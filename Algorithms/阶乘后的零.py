#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 23:01:23 2018

@author: pineapple
"""

'''
别人的：　时间复杂度O(logn) 空间复杂度O(n)
思路：所有５的倍数会加１个０，２５的倍数会加２个０，
    １２５的倍数会加３个０，...　
    所以就先统计不大于ｎ的数中有哪些５的幂指数(比如：５，２５，１２５...)
    然后再统计不大于ｎ的数中这些幂指数的倍数，
    然后再统计计算０的个数
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        point = 5
        
        five_power = 0
        while point <= n:
            five_power += 1
            point = point * 5
        five_count = []
        for i in range(five_power):
            five_count.append(n//5**(i+1))
        for i in range(len(five_count)-1):
            five_count[i] -= five_count[i+1]
        ans = 0
        for i in range(len(five_count)):
            ans += five_count[i]*(i+1)
        return ans

'''
最简洁的代码，也是上面的思路
'''    
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n = n//5
            res += n
        return res
