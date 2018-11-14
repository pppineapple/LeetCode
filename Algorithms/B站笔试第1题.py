#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 14:33:42 2018

@author: pineapple
"""

'''
B站笔试第１题：
找最多的能认识的盆友数量，DFS或BFS都能解
注意边界条件，没有一个盆友
'''

def friend_to_dict(friend):
    meethash = {}
    for f in friend:
        if f[0] not in meethash:
            meethash[f[0]] = [f[1]]
        else:
            meethash[f[0]].append(f[1])
        if f[1] not in meethash:
            meethash[f[1]] = [f[0]]
        else:
            meethash[f[1]].append(f[0])
    return meethash

def DFS(graph, s):
    if s not in graph:
        return 0
    stack = [s]
    seen = set([s])
    while stack != []:
        node = stack.pop()
        for i in graph[node]:
            if i not in seen:
                stack.append(i)
                seen.add(i)
    count = 0
    for i in seen:
        if i not in graph[s] and i != s:
            count += 1
    return count

while True:
    try:
        n = int(raw_input().split()[0])
        a = int(raw_input().split()[0])
        meet = int(raw_input().split()[0])
        friend = []
        for i in range(meet):
            f = map(int, raw_input().split(','))
            friend.append(f)
        graph = friend_to_dict(friend)
        print DFS(graph, a)
    except:
		break