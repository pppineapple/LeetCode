# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:47:38 2018

@author: xiaohong
"""

'''
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''


'''
我的 best 1
思路：将目标字符串映射到一个hash表(字典，值为字符个数)中,然后遍历hash表，如果字符个数大于
        杂志字符串个数，就返回False
'''
def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        rhash = {}
        for i in ransomNote:
            if i not in rhash:
                rhash[i] = 1
            else:
                rhash[i] += 1
        
        for word in rhash:
            if rhash[word] > magazine.count(word):
                return False
        return True
                        