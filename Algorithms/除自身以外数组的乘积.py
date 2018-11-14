#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 11:16:45 2018

@author: pineapple
"""

'''
别人的：时间复杂度O(n) 空间复杂度O(n)
由于不能使用除号，所以必须只有乘号来计算。
维护两个数组dp1和dp2，分
别用来保存第i个位置之前所有数的乘积和第i个位置之后所有数的乘积。
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        dp1 = [1]
        dp2 = [1]
        for i in  range(len(nums)-1):
            dp1.append(dp1[i] * nums[i])
            dp2.append(dp2[i] * nums[-i-1])
            
        result = []
        for j in range(len(dp1)):
            result.append(dp1[j]*dp2[-j-1])
        return result
    
    
'''
更简洁的代码：　时间复杂度O(n) 空间复杂度O(1)
这里也是利用第i个位置的元素前面元素乘积乘上后面元素乘积
只不过用了两次循环，第一次循环顺着遍历，得到低i个位置之前的元素乘积数组
然后第二遍反着遍历，直接在数组output上修改乘上第i个位置之后的元素的乘积
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = []
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
        
        p = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] = output[j] * p
            p = p * nums[j]
        return output



    
nums = [1,2,3,4]
s = Solution()
s.productExceptSelf(nums)