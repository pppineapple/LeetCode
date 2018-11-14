# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:48:12 2018

@author: xiaohong
"""

'''
设计循环队列，满足一下属性和方法

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
'''


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.length = k
        self.items = []
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.items)+1 <= self.length:
            self.items.append(value)
            return True
        else:
            return False
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.items != []:
            self.items.pop(0)
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.items == []:
            return -1
        else:
            return self.items[0]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.items == []:
            return -1
        else:
            return self.items[-1]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.items == []
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return len(self.items) >= self.length