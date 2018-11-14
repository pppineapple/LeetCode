# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 08:28:36 2018

@author: xiaohong
"""
'''
有效的字母异位词 
'''


'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
'''

'''
我的 68ms
'''

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        i = 0
        done = True
        while i < len(slist) and done:
            if slist[i] == tlist[i]:
                i += 1
            else:
                done = False
                
        return done


'''
best: 36ms
'''
            
def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """    
    
        if len(s) != len(t):
            return False
        
        ss = set(s)
        
        for i in ss:
            if s.count(i) != t.count(i):
                return False
        return True
    
'''
第三次做：思路hash表
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hash = {}
        for i in s:
            hash[i] = hash.get(i, 0) + 1
        
        for j in t:
            if j in hash and hash[j] > 0:
                hash[j] -= 1
            else:
                return False
        return True