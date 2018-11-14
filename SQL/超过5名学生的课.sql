#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 12:55:07 2018

@author: pineapple
"""

'''
有一个courses 表 ，有: student (学生) 和 class (课程)。

请列出所有超过或等于5名学生的课。

例如,表:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
应该输出:

+---------+
| class   |
+---------+
| Math    |
+---------+
Note:
学生在每个课中不应被重复计算。
'''


# Write your MySQL query statement below
select a.class
from 
(select count(distinct Student) as sc,class from courses group by class) a
where a.sc >= 5