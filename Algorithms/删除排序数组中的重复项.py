# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:03:25 2018

@author: xiaohong
"""

'''
给定一个排序数组，你需要在原地删除重复出现的元素，
使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素
'''



'''
我的代码 116ms
'''
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                nums.pop(index)
            else:
                index += 1
            
        return len(nums)    
    
    


'''
第二次的思路： 时间复杂度O(n) 空间复杂度O(1)
原地修改数组，快指针i,慢指针j,因为是递增数组，如果 nums[j] > nums[i]
慢指针i向前移动一位，同时将nums[i]赋值为nums[j],再移动慢指针j
如果nums[j] <= nums[i],　只移动快指针
最后返回慢指针＋１

'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] > nums[i]:
                i += 1
                nums[i] = nums[j]
                j += 1
                
            else:
                j += 1
        return i+1