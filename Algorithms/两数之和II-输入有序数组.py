# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:02:37 2018

@author: xiaohong
"""

'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''

'''
别人的 0.99
思路：
我们可以这样想，我们首先判断首尾两项的和是不是target，
如果比target小，那么我们左边+1位置的数（比左边位置的数大）再和右相相加，继续判断。
如果比target大，那么我们右边-1位置的数（比右边位置的数小）再和左相相加，继续判断。
我们通过这样不断放缩的过程，就可以在O(n)的时间复杂度内找到对应的坐标位置。
（这和快速排序的思路很相似）
'''


def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s  == target:
                return [i+1, j+1]
            elif s > target:
                j = j -1
            else:
                i = i+1
            

twoSum(a,9)


a = [2,7,11,15]
a[:2]
a[3:]
