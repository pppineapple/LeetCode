# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:42:41 2018

@author: xiaohong
"""

graph = {'A':['B','C'],
         'B':['A','C','D'],
         'C':['A','B','E'],
         'D':['B','C','E','F'],
         'E':['C','D'],
         'F':['D']
        }


'''
广度优先搜素
队列
'''

def BFS(graph, s):
    queue = [s]
    seen = set([s])
    while queue != []:
        node = queue.pop(0)
        print node
        for i in graph[node]:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                
BFS(graph, 'F')        
        
'''
深度优先搜素
栈
'''
def DFS(graph, s):
    stack = [s]
    seen = set([s])
    while stack != []:
        node = stack.pop()
        print node
        for i in graph[node]:
            if i not in seen:
                stack.append(i)
                seen.add(i)
                
DFS(graph, 'B')

'''
最短路径，通过BFS
'''
def sortSearch(graph, s, e):
    queue = [s]
    seen =  set([s])
    parent = {s:None}
    while queue != []:
        vertex = queue.pop(0)
        print vertex
        for i in graph[vertex]:
            if i not in seen:
                parent[i] = vertex
                queue.append(i)
                seen.add(i)
    
    eParent = parent[e]
    count = 1
    while eParent != s:
        eParent = parent[eParent]
        count += 1
    print count
sortSearch(graph, 'A', 'F')

'''
最短路径，通过BFS和优先队列 priority queue
'''

import heapq
pqueue = []
heapq.heappush(pqueue, (1, 'A'))
heapq.heappush(pqueue, (7, 'B'))
heapq.heappush(pqueue, (4, 'C'))
heapq.heappush(pqueue, (2, 'D'))
heapq.heappop(pqueue)
heapq.heappop(pqueue)

graph = {'A':{'B':5,'C':1},
         'B':{'A':5,'C':2,'D':1},
         'C':{'A':1,'B':2,'E':8},
         'D':{'B':1,'C':4,'E':3,'F':6},
         'E':{'C':8,'D':3},
         'F':{'D':6}
        }



def mostShortSearch(garph, s):
    import heapq
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    parent = {s:None}
    distance = {s : 0}
    seen = set([s])
    while pqueue != []:
        vertex = heapq.heappop(pqueue)
        for i in graph[vertex[1]]:
            if i not in seen:
                distance_i = graph[vertex[1]][i] + vertex[0]
                heapq.heappush(pqueue, (distance_i, i))
                parent[i] = vertex[1]
                distance[i] = distance_i
        seen.add(vertex[1])
    print parent
    print distance

   
mostShortSearch(graph, 'B')



def mostShortSearch(garph, s):
    import heapq
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    parent = {s:None}
    distance = {s : 0}
    for k in graph.keys():
        if k != s:
            distance[k] = float('inf')
    seen = set([s])
    while pqueue != []:
        pair = heapq.heappop(pqueue)
        vertex = pair[1]
        dist = pair[0]
        for i in graph[vertex]:
            if i not in seen:
                distance_i = graph[vertex][i] + dist
                if distance_i < distance[i]:
                    heapq.heappush(pqueue, (distance_i, i))
                    parent[i] = vertex
                    distance[i] = distance_i
        seen.add(vertex)
    print parent
    print distance


{'B':5}.keys()



a = set(['a'])
a.add('b')
a.add('c')
a.add('a')
a
