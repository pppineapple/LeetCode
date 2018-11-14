# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:11:17 2018

@author: xiaohong
"""

'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
'''

'''
我的代码 32ms
'''
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        charLen = [len(char) for char in strs]
        minLen = min(charLen)
        print minLen
        minLenStr = strs[charLen.index(minLen)]
        if minLenStr == '':
            return ''
        
        strs.remove(minLenStr)
        if strs == []:
            return minLenStr
        
        index = 0
        still_equal = True
        char_equal = ''
        while index < len(minLenStr) and still_equal:
            print index
            for Char in strs:
                if Char[index] != minLenStr[index]:
                    still_equal = False
            if still_equal:
                char_equal = char_equal + minLenStr[index]
                index += 1

        return char_equal
    
'''
我的另一个代码
我的：时间复杂度O(n^2) 空间复杂度O(1)
思路：　先遍历数组，找到最短的字符shorter，然后两层循环
    外循环shorter,内循环数组strs，如果出现数组字符串中的字符与shorter的字符不同
    那就返回shorter[:i]
'''    

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        shortlen = float('inf')
        shorter = ''
        for s in strs:
            if len(s) < shortlen:
                shortlen = len(s)
                shorter = s
        if shorter == '':
            return ''
        for i in range(len(shorter)):
            for j in strs:
                if shorter[i] != j[i] and i == 0:
                    return ''
                elif shorter[i] != j[i]:
                    return shorter[:i]


        return shorter[:i+1]
    
    
'''
best： 24ms
'''
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
      # 判断是否为空
        if not strs:
            return ''
        # 在使用max和min的时候已经把字符串比较了一遍
        # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最小的字符串
        s1 = min(strs)
        # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最大的字符串
        s2 = max(strs)
        # 使用枚举变量s1字符串的每个字母和下标
        for i, c in enumerate(s1):
            print i, c
            # 比较是否相同的字符串，不相同则使用下标截取字符串
            if c != s2[i]:
                return s1[:i]
        return s1
    
    
'''
我的　时间复杂度O(nk) 空间复杂度O(1)
思路：把最小字符串长度找出来，然后找不同
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        elif len(set(strs)) == 1:
            return strs[0]
        minlen = min([len(i) for i in strs])
        for j in range(minlen):
            c = strs[0][j]
            for u in range(1, len(strs)):
                if strs[u][j] != c:
                    if j < 0:
                        return ''
                    return strs[0][:j] 

        return strs[0][:minlen]
'''
别人的另外一种思路：直接把最小长度的字符串和最大长度的字符串拿出来比较
'''    
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        maxstr = max(strs)
        minstr = min(strs)
        for i in range(len(minstr)):
            if minstr[i] != maxstr[i]:
                if i == 0:
                    return ''
                else:
                    return minstr[:i]
        return minstr