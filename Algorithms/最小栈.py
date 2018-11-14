#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:53:48 2018

@author: pineapple
"""

'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''

'''
我的 72ms
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.items == []:
            stack_min = x
        else:
            stack_min = min(self.items[-1][0], x)
        self.items.append((stack_min, x))

    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items)-1][1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.items[len(self.items)-1][0]


'''
best 56ms
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min_item = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.append(x)
        if self.min_item == []:
            self.min_item.append(x)
        else:
            self.min_item.append(min(self.min_item[-1], x))

    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()
        self.min_item.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items)-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_item[-1]