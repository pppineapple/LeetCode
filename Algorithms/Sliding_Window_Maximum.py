#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:54:37 2018

@author: pineapple
"""

'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？
'''

'''
我的：　时间复杂度O(nk) 空间复杂度O(k)
思路：直接构建长度为k的滑块，然后每一次向右滑动时
    都找出其中的最大值，加入到ans末端。
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        left = 0
        right = left+k
        ans = []
        while right <= len(nums):
            tmp = nums[left:right]
            max_tmp = max(tmp)
            ans.append(max_tmp)
            left += 1
            right += 1
        return ans
    

'''
更巧妙的思路：时间复杂度O(n) 空间复杂度O(k)
思路：利用双端队列deque
遍历数组nums，使用双端队列deque维护滑动窗口内有可能成为最大值元素的数组下标

由于数组中的每一个元素至多只会入队、出队一次，因此均摊时间复杂度为O(n)

记当前下标为i，则滑动窗口的有效下标范围为[i - (k - 1), i]

若deque中的元素下标＜ i - (k - 1)，则将其从队头弹出，deque中的元素按照下标递增顺序从队尾入队。

这样就确保deque中的数组下标范围为[i - (k - 1), i]，满足滑动窗口的要求。

当下标i从队尾入队时，顺次弹出队列尾部不大于nums[i]的数组下标（这些被弹出的元素由于新元素的加入而变得没有意义）

deque的队头元素即为当前滑动窗口的最大值    
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans
    
hash = {1:4,2:3,3:2,5:1}
max(hash)
import collections
dq = collections.deque()
dq.append(0)
dq.append(-1)
print dq
dq[0]
