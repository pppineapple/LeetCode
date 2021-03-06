#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:52:17 2018

@author: pineapple
"""

/*
'''
Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department 表包含公司所有部门的信息。

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
编写一个 SQL 查询，找出每个部门工资最高的员工。例如，根据上述给定的表格，Max 在 IT 部门有最高工资，Henry 在 Sales 部门有最高工资。

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
'''

'''
思路：把每个部门最大的 salary，id 查出来，然后去匹配职员的名字和部门名字
'''
*/

# Write your MySQL query statement below
select d.Name as Department, e.Name as Employee, e.Salary
from Employee e, 
(select DepartmentId, max(Salary) as max_salary from Employee group by DepartmentId) a,
Department d
where e.DepartmentId = a.DepartmentId and e.Salary = a.max_salary and d.Id = e.DepartmentId
