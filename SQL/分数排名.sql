#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:33:31 2018

@author: pineapple
"""

'''
编写一个 SQL 查询来实现分数排名。如果两个分数相同，则两个分数排名（Rank）相同。
请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
例如，根据上述给定的 Scores 表，你的查询应该返回（按分数从高到低排列）：

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
'''


# Write your MySQL query statement below

#解法１ 子查询
select s.Score, (select count(distinct Score) from Scores where Score >= s.Score) as Rank
from Scores s order by Score DESC

#解法２　内联inner join
select s1.score, count(distinct s2.score) as Rank
from Scores s1
inner join Scores s2 on s1.score <= s2.score
group by s1.id order by s1.score DESC

#解法３  设置变量
select Score ,
@rank := @rank + (@pre <> (@pre := Score)) as Rank
from Scores, (select @rank:=0, @pre:=-1) INIT
order by score DESC