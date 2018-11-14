# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:54:12 2018

@author: xiaohong
"""

'''
颜色分类
'''

'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，
原地对它们进行排序，使得相同颜色的元素相邻，
并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
'''


def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 冒泡排序
#        for passnum in range(len(nums)-1, 0, -1):
#            for i in range(passnum):
#                if nums[i] > nums[i+1]:
#                    tmp = nums[i]
#                    nums[i] = nums[i+1]
#                    nums[i+1] = tmp
        
        # 选择排序
#        for passnum in range(len(nums)-1, 0, -1):
#            maxnum = max(nums[:passnum+1])
#            maxindex = nums.index(maxnum)
#            tmp = nums[maxindex]
#            nums[maxindex] = nums[passnum]
#            nums[passnum] = tmp
            
        # 插入排序
#        for index in range(1, len(nums)):
#            currentValue = nums[index]
#            position = index
#            while position > 0 and nums[position-1] > currentValue:
#                nums[position] = nums[position-1]
#                position -= 1
#            nums[position] = currentValue

        # shell 排序
#        def insertGapSort(nums,start,gap):
#            for index in range(start+gap, len(nums), gap):
#                currentValue = nums[index]
#                position = index
#                while position >= gap and nums[position-gap] > currentValue:
#                    nums[position] = nums[position-gap]
#                    position -= gap
#                nums[position] = currentValue
        
#        subCount = len(nums) // 2
#        while subCount > 0:
#            for startposition in range(subCount):
#                insertGapSort(nums, startposition, subCount)
#            subCount = subCount // 2

        # 归并排序
#        if len(nums) > 1:
#            mid = len(nums) // 2
#            lefthalf = nums[:mid]
#            righthalf = nums[mid:]
            
#            self.sortColors(lefthalf)
#            self.sortColors(righthalf)
            
#            i = 0
#            j = 0
#            k = 0
            
#            while len(lefthalf) > i and len(righthalf) > j:
#                if lefthalf[i] > righthalf[j]:
#                    nums[k] = righthalf[j]
#                    j = j+1
#                else:
#                    nums[k] = lefthalf[i]
#                    i = i+1
#                k = k+1
#            while len(lefthalf) > i:
#                nums[k] = lefthalf[i]
#                i = i+1
#                k = k+1
#            while len(righthalf) > j:
#                nums[k] = righthalf[j]
#                j = j+1
#                k = k+1

        # 快速排序
        def partition(nums, first, last):
            pivotValue = nums[first]
            leftmark = first + 1
            rightmark = last
            done = False
            while not done:
                while leftmark <= rightmark and nums[leftmark] <= pivotValue:
                    leftmark += 1
                while rightmark >= leftmark and nums[rightmark] >= pivotValue:
                    rightmark -= 1
                if rightmark > leftmark:
                    tmp = nums[leftmark]
                    nums[leftmark] = nums[rightmark]
                    nums[rightmark] = tmp
                else:
                    done = True
            tmp = nums[first]
            nums[first] = nums[rightmark]
            nums[rightmark] = tmp
            
            return rightmark
        
        def quickSortHelper(nums, start, last):
            if start < last:
                splitposition = partition(nums, start, last)
                quickSortHelper(nums, start, splitposition-1)
                quickSortHelper(nums, splitposition+1, last)
        
        quickSortHelper(nums, 0, len(nums)-1)
        
        
'''
三指针分割法：时间复杂度O(n)　空间复杂度O(1)
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = 0
        zero_end = -1
        one_end = n
        while i < one_end:
            if nums[i] == 0:
                zero_end += 1
                tmp = nums[zero_end]
                nums[zero_end] = nums[i]
                nums[i] = tmp
                i+=1
            elif nums[i] == 2:
                one_end -= 1
                tmp = nums[one_end]
                nums[one_end] = nums[i]
                nums[i] = tmp
            else:
                i += 1
                
'''
第二次做：没做出来
三指针：zero_end表示0的结束位置
        one_end表示1的结束位置
        i表示0和1的位置，循环出口条件是i>=one_end
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_end = -1
        one_end = len(nums)
        i = 0
        while i < one_end:
            if nums[i] == 2:
                one_end -= 1
                tmp = nums[i]
                nums[i] = nums[one_end]
                nums[one_end] = tmp
            elif nums[i] == 0:
                zero_end += 1
                tmp = nums[zero_end]
                nums[zero_end] = nums[i]
                nums[i] = tmp
                i += 1
            else:
                i += 1
            