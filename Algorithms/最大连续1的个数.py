# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:24:59 2018

@author: xiaohong
"""

'''
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
'''

'''
我的  时间复杂度O(n) 空间复杂度O(1) 0.81
思路： 双指针，最大连续1计数的计算就是快指针减去慢指针，
        然后设置一个变量表示最大连续1计数，然后用max函数保持更新
        
'''
def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        max_continue = 0
        while j < len(nums):
            if nums[j] == 1:
                j += 1
            else:
                max_continue = max(max_continue, j-i)
                j += 1
                i = j
                
        if j > i:
            max_continue = max(max_continue, j-i)
        return max_continue
    
    
'''
更简洁的代码：
思路： 因为这里是二进制数组，元素不是1就是0,所以不需要双指针，只需要设置一个统计1
        的变量count就行了
'''

def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_continue = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_continue = max(max_continue, count)
                count = 0
        return max(max_continue, count)
        
        