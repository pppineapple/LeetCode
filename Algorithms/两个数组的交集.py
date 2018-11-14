# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 17:40:28 2018

@author: xiaohong
"""

'''
给定两个数组，写一个函数来计算它们的交集。

例子:
给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

提示:
每个在结果中的元素必定是唯一的。
我们可以不考虑输出结果的顺序。
'''

'''
我的 84ms
'''
def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        output = []
        for i in set1:
            for j in set2:
                if i == j:
                    output.append(i)
        return output
        

nums1 = [4,7,9,7,6,7]
nums2 = [5,0,0,6,1,6,2,2,4]
intersection(nums1, nums2)

'''
best 24ms
'''
def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return list(set(nums1) & set(nums2))
    
