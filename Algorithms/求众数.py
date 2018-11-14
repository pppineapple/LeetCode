#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 09:10:38 2018

@author: pineapple
"""

'''
给定一个大小为 n 的数组，找到其中的众数。
众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

'''
'''
我的：　时间复杂度O(n) 空间复杂度O(n)
思路：用hash表储存元素出现次数，然后遍历hash表，返回次数大于len(nums)//2的元素
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1            
        for j in hash:
            if hash[j] > len(nums) // 2:
                return j
'''
跟简洁的写法：　时间复杂度O(n) 空间复杂度O(n)
因为 max(iterable,key,default).s求迭代器的最大值，
其中iterable 为迭代器，max会for i in … 遍历一遍这个迭代器，
然后将迭代器的每一个返回值当做参数传给key=func 
其中的func(一般用lambda表达式定义) ，然后将func的执行结果传给key，
然后以key为标准进行大小的判断。
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1          
        return max(hash.items(), key=lambda x: x[1])[0]


'''
第二次做　时间复杂度O(nlogn) 空间复杂度(1)
思路：对数组排序，因为众数是数量超过n//2的数，那么排序后数组最终健的位置一定是众数
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]