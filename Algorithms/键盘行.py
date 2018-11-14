#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:14:03 2018

@author: pineapple
"""
'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。
键盘如下图所示。


American keyboard

示例1:
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
注意:

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
不考虑大写情况
'''

'''
我的：时间复杂度Ｏ(n^2)　空间负责度Ｏ(1)
思路：通过计数来判断每一个单词的每一个字符是否都来自同一行
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lowalph = 'abcdefghijklmnopqrstuvwxyz'
        
        lowalph1 = 'qwertyuiop'
        lowalph2 = 'asdfghjkl'
        lowalph3 = 'zxcvbnm'
        
        result = []
        for word in words:
            if word[0] not in lowalph and (word[0] not in lowalph2 or word[0] not in lowalph3):
                count1 = 0
                count2 = 0
                count3 = 0
                found = True
                for i in word[1:]:
                    if i in lowalph1:
                        count1 += 1
                    if i in lowalph2:
                        count2 += 1
                    if i in lowalph3:
                        count3 += 1
                    if (count1 > 0 and count2 > 0) or (count2>0 and count3>0) or (count1 > 0 and count3>0):
                        found = False
                        break
                if found:
                    result.append(word)
            elif word[0] in lowalph:
                count1 = 0
                count2 = 0
                count3 = 0
                found = True
                for i in word:
                    if i in lowalph1:
                        count1 += 1
                    if i in lowalph2:
                        count2 += 1
                    if i in lowalph3:
                        count3 += 1
                    if (count1 > 0 and count2 > 0) or (count2>0 and count3>0) or (count1 > 0 and count3>0):
                        found = False
                        break
                if found:
                    result.append(word)
        return result

'''
更优雅的代码：　通过hash表来建立映射，遍历单词时，一旦映射不同就break
'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        alph = {}
        for w in 'qwertyuiop':
            alph[w] = 1
        for w in 'asdfghjkl':
            alph[w] = 2
        for w in 'zxcvbnm':
            alph[w] = 3
        result = []
        for word in words:
            found = True
            k = alph[word[0].lower()]
            for i in word[1:]:
                if alph[i.lower()] != k:
                    found = False
                    break
            if found:
                result.append(word)
        return result
    
'''
一下是考虑了大写的情况
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lowalph = 'abcdefghijklmnopqrstuvwxyz'
        alph = {}
        for w in 'qwertyuiop':
            alph[w] = 1
        for w in 'asdfghjkl':
            alph[w] = 2
        for w in 'zxcvbnm':
            alph[w] = 3
        
        result = []
        for word in words:
            found = True
            if word[0] not in lowalph and alph[word[0].lower()] == 1:
                found = False
            else:
                k = alph[word[0].lower()]
                for i in word[1:]:
                    if alph[i] not in lowalph and alph[alph[i].lower()] == 1:
                        found = False
                        break
                    if alph[i.lower()] != k:
                        found = False
                        break
            if found:
                result.append(word)
        return result
words = ["Hello","Alaska","Dad","Peace"]
s = Solution()
s.findWords(words)                        
word = words[1]
