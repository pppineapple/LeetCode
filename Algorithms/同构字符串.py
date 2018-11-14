# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:41:32 2018

@author: xiaohong
"""


'''
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。
两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:
输入: s = "egg", t = "add"
输出: true

示例 2:
输入: s = "foo", t = "bar"
输出: false

示例 3:
输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
'''

'''
别人的 0.97
思路： 利用哈希表映射(python里面是字典)
        建立s中每个字符对t的映射，如果重复映射的值不同，那就不是可替换的
        最后要判断一下hash表中val的去重长度和哈希表长度是否相同
'''


def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False
        hashval = [hashmap[k] for k in hashmap]
        return len(hashmap) == len(set(hashval))
                
        