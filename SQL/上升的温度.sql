#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:35:41 2018

@author: pineapple
"""

'''
给定一个 Weather 表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 Id。

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
例如，根据上述给定的 Weather 表格，返回如下 Id:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+
'''

'''
思路：对自己两个表进行比较，然后在where中进行条件筛选
'''
# Write your MySQL query statement below
select w.Id
from Weather w, Weather w1
where datediff(w.RecordDate,w1.RecordDate) = 1 and w.Temperature > w1.Temperature