# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:07:57 2018

@author: xiaohong
"""

'''
移除元素
'''

'''
给定一个数组 nums 和一个值 val，
你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。
'''

'''
我的代码：32ms
'''
def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop()
            else:
                index = index + 1
        return index
    
removeElement([2,2,3,3], 3)

'''
再做一遍的思路:　时间复杂度O(n) 空间复杂度O(1)
思路：　双指针原地维护数组
只要把数组中所有的与val不相等的元素，按顺序给数组的前段元素位赋值，
最后只要返回慢指针的值就行了
双指针，慢指针维护数组前段被赋值的元素，快指针维护赋值的元素
    如果快指针的元素不为val，就将该元素赋值到慢指针处，
    快慢指针同时前进１
    如果快指针的元素为val，快指针前进１，慢指针不动
    直到快指针到达数组末端
    最后从慢指针的值就是数组移除val元素之后的长度(其实并没有真正移除val)
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i