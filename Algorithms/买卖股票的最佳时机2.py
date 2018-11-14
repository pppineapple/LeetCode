# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 07:52:46 2018

@author: xiaohong
"""

'''

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        begin_price = prices[0]
        profit = 0
        for p in begin_price:
            if p > begin_price:
                profit += p - begin_price
                begin_price = p
            else:
                begin_price = min(p, begin_price)
                
        return profit
        
'''
第二次做：时间复杂度O(n) 空间复杂度O(1)
思路：和购买股票的最佳时机１一样的做法，
只不过卖完股票之后要重置股票购买价格为当前卖出价格
因为是多次购买，所以不需要用对profit取max，而是取累加
'''        
        
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        bprice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if bprice > prices[i]:
                bprice = prices[i]
            else:
                profit += prices[i] - bprice
                bprice = prices[i]
        return profit
                            