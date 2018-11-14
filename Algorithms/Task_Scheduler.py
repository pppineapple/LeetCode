#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:11:56 2018

@author: pineapple
"""

'''
给定一个用字符数组表示的 CPU 需要执行的任务列表。
其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。C
PU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，
因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
'''


'''
别人的：　时间复杂度O(n) 空间复杂度O(n)
思路：把任务频率数最大的任务取出来，先排开，间隔是任务间隔数n
    比如：　['A','A','A','A','A','B',B',B',B',B','C',C',C',C','D','D','E']
    A o o o o o A o o o o o A o o o o o A o o o o o A x x x x x
    然后再插入频率第二大的，以此类推。i表示cpu休息时间
    A B C D E i A B C D i i A B C i i i A B C i i i A B
    所以就可以用公式计算：(k-1)*(n+1)+p
    其中k表示频率最大任务的频率数，而有效的分组数group_num就是 k-1
    n表示同任务间隔时间，那么每组的时间长度就是 n+1
    p表示频率最高的任务的种类。比如上例是AB，p=2
    最后计算出来的时间要任务数的长度比较一下，取最大
    这是因为：如果n<len(set(tasks))，就表示任务可以直接补考虑任务间隔数，直接排
'''

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskhash = {}
        for task in tasks:
            taskhash[task] = taskhash.get(task, 0) + 1
        group_num = max(taskhash.values()) - 1
        group_len = n + 1
        p = taskhash.values().count(max(taskhash.values()))
        return max(len(tasks), group_num*group_len+p)
