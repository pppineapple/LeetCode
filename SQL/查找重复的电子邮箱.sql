#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:35:23 2018

@author: pineapple
"""
/*
'''
编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。

示例：

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
根据以上输入，你的查询应返回以下结果：

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
说明：所有电子邮箱都是小写字母。
'''
*/
# Write your MySQL query statement below
select a.Email
from 
(select Email, count(Email) as e_count from Person group by Email) as a
where a.e_count > 1
