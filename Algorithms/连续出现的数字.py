#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:52:18 2018

@author: pineapple
"""

'''
编写一个 SQL 查询，查找所有至少连续出现三次的数字。

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
'''


# Write your MySQL query statement below

select distinct l1.Num as ConsecutiveNums
from Logs l1 
left join Logs l2 on l2.Id = l1.Id + 1
left join Logs l3 on l3.Id = l1.Id + 2
where l1.Num = l2.Num and l1.Num = l3.Num