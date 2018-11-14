#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:05:59 2018

@author: pineapple
"""

'''
编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id 是这个表的主键。
例如，在运行你的查询语句之后，上面的 Person 表应返回以下几行:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
'''

'''
思路：将Person和自己比较，然后删除email重复的并且id大的
'''

delete p1
from Person p1, Person p2
where p1.Email = p2.Email and p1.id > p2.id