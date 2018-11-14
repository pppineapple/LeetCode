#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:02:34 2018

@author: pineapple
"""

'''
给定两个单词（beginWord 和 endWord）和一个字典，
找到从 beginWord 到 endWord 的最短转换序列的长度。
转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。
'''


'''
别人的思路：s时间复杂度O(nlogn) 空间复杂度O(n)
思路：首先写一个辅助函数nextValidWord用来找可以变换的相邻word,
    这个函数返回相邻word的列表，注意每找到一个有效的相邻变换word
    那么wordList中就要删除掉这个word，表示后面不在找那些已经找到过的word了
    然后写一个辅助函数BFS用来找endWord
    具体就是利用队列queue来实现，这里因为问题是求变换的step
    所以直接把step保留在每一次查找的queue中
最后需要注意的是：如果不讲wordList转化为hash表，那么在查找相邻变换word时：
    删除已经找到过的word会很慢，所以不如以空间换时间，建立hash表
    那么在删除时就只有O(1)的时间复杂度。
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = {}
        for w in wordList:
            wordDict[w] = True
        return self.BFS(beginWord, endWord, wordDict)

    def nextVaildWord(self, word, wordList):
        ValidWord = []
        for i in range(len(word)):
            tmp = list(word)
            for j in range(ord('a'), ord('z')+1):
                tmp[i] = chr(j)
                tmp_word = ''.join(tmp)
                if tmp_word in wordList:
                    ValidWord.append(tmp_word)
                    wordList.pop(tmp_word)
        return ValidWord

    def BFS(self, beginWord, endWord, wordList):
        queue = [[beginWord, 1]]
        while queue != []:
            tmp = queue.pop(0)
            word, step = tmp[0], tmp[1]
            nextWords = self.nextVaildWord(word, wordList)
            if endWord in nextWords:
                return step + 1
            else:
                for w in nextWords:
                    queue.append([w, step+1])
        return 0
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

s = Solution()
s.ladderLength(beginWord, endWord, wordList)
