#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 18:34:03 2018

@author: pineapple
"""

'''
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。


'''

'''
别人的：　时间复杂度O(n) 空间复杂度O(n)
思路：动态规划，直接构造出长度为amount+1的数组opt
    opt[i]就表示零钱为i的时候对应的硬币数最少的个数
    opt[0] = 0, opt[i] = float('inf')
    这里就有递推公式：opt[i+coin] = min(opt[i+coin], opt[i]+1)
    这个递推是从前往后推
    最后返回opt[-1],如果是'inf'就返回-1表示不能找零
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        opt = [0] + [float('inf')]*amount
        for i in range(amount+1):
            for coin in coins:
                if i + coin <= amount:
                    opt[i+coin] = min(opt[i+coin], opt[i]+1)
 
        if opt[-1] == float('inf'):
            return -1
        else:
            return opt[-1]