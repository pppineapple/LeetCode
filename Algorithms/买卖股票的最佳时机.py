# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 11:35:29 2018

@author: xiaohong
"""

'''
买卖股票的最佳时机
'''

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），
设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


'''
别人的 28ms
'''


def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            buy = min(prices[i], buy)
            if profit < prices[i] - buy:
                profit = prices[i] - buy
        return profit

        
maxProfit([7,1,5,3,6,4])

'''
第二次做：时间复杂度O(n)　空间复杂度O(1)
思路：动态规划，因为只能购买一次，
    直接用buy变量来记录购买的价格，profit记录最大的利润
    
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = max(profit, prices[i]-buy)
        return profit
        
  