# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 18:05:58 2018

@author: xiaohong
"""


'''
别人 1
思路：
巧妙用了set（）,判断每个单词的除去倒数第一个字母是否在set里，用一个变量保存最长的单词。

用判断新单词是否比最长单词更长的方式完成两个需求：
1.找出最长；
2.同样最长的情况下，保留字母序最小的。这样做的前提是先对words进行排序。

'''

def longestWord(words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        res = set([''])
        longestWord = ''
        for word in words:
            if word[:-1] in res:
                res.add(word)
                if len(word) > len(longestWord):
                    longestWord = word
        return longestWord
 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]    
words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]  
words = ["w","wo","wor","worl","world"]     
longestWord(words)
