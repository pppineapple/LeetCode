#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:18:19 2018

@author: pineapple
"""

'''
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''


'''
别人的思路：时间复杂度O(nk) 空间复杂度O(k)
自己的代码:
    先对t建立subhash表来表示t中元素和元素个数的对应关系
    利用滑块移动思想，用left表示滑块移动的左边界，遍历数组nums的i表示滑块移动的右边界
    先固定left不动，向右移动i，如果nums[i]出现在subhash中，并且subhash中对应元素个数大于0
    计数器tcount += 1，表示在[left:i+1]区间上已经找到一个正确的t中的元素了
    当tcount == len(t)时，表示[left:i+1]区间就是包含了t所有元素的子串
    这时用一个全局变量max_len，和max_sub来记录最小的子串和最小的子串长度
    然后移动left，同理也是：如果nums[left]出现在subhash中，并且subhash[nums[left]]==0
    就说明现在抛弃的left位置的元素是t中的元素，所以 tcount -= 1
    subhash[nums[left]] += 1,
    如果　tcount != len(t)，这个时候又要移动右边界指针i了
    
需要注意的一些边界条件：
1.s和t的长度相等，这就直接利用hash表来判断s和t的元素－个数对是否一致
2.如果s中没有符合条件的t，需要输出空字符''
    所以一开始我是设定min_len = len(s)+1 和　min_sub = ''
    
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == len(t):
            shash = {}
            for i in s:
                shash[i] = shash.get(i, 0)+1
            thash = {}
            for i in t:
                thash[i] = thash.get(i, 0)+1
            if shash == thash:
                return s
            else:
                return ''
        subhash = {}
        for i in t:
            subhash[i] = subhash.get(i, 0)+1      
        min_len = len(s)+1
        min_sub = ''
        tcount = 0
        left = 0
        for i in range(len(s)):         
            if s[i] in subhash:
                if subhash[s[i]] > 0:
                    tcount += 1
                subhash[s[i]] -= 1
            while tcount == len(t) and left <= i:
                if min_len > i - left + 1:
                    min_len = i-left+1
                    min_sub = s[left:i+1]
                if s[left] in subhash:
                    if subhash[s[left]] == 0:
                        tcount -= 1
                    subhash[s[left]] += 1    
                left += 1
        return min_sub
    
s = "ADOBECODEBANC"
t = "ABC"
s = 'abcde'
t = 'ef'
s = 'abc'
t = 'a'
s = "babb"
t = "baba"
s = 'aa'
t = 'aa'
S =Solution()
S.minWindow(s,t)


