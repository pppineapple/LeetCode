# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:06:26 2018

@author: xiaohong
"""


'''

A、B两伙马贼意外地在一片沙漠中发现了一处金矿，双方都想独占金矿，
但各自的实力都不足以吞下对方，经过谈判后，
双方同意用一个公平的方式来处理这片金矿。
处理的规则如下：他们把整个金矿分成n段，
由A、B开始轮流从最左端或最右端占据一段，直到分完为止。 

马贼A想提前知道他们能分到多少金子，因此请你帮忙计算他们最后各自拥有多少金子?
（两伙马贼均会采取对己方有利的策略）


输入
测试数据包含多组输入数据。输入数据的第一行为一个正整数T(T<=20)，
表示测试数据的组数。然后是T组测试数据，每组测试数据的第一行包含一个整数n，
下一行包含n个数（n <= 500 ），表示每段金矿的含金量，保证其数值大小不超过1000。


样例输入
2 
6
4 7 2 9 5 2
10
140 649 340 982 105 86 56 610 340 879

输出
对于每一组测试数据，输出一行"Case #id: sc1 sc2"，
表示第id组数据时马贼A分到金子数量为sc1，马贼B分到金子数量为sc2。详见样例。

样例输出
Case #1: 18 11
Case #2: 3206 981
'''


n = map(int, raw_input().split())[0]
case_n = []
case_info = []
for i in range(n):
	case_i = map(int, raw_input().split())[0]
	case_i_info = map(int, raw_input().split(' '))
	case_n.append(case_i)
	case_info.append(case_i_info)

    
def compute(case_n, case_info):    
    opt = [[0]*case_n for i in range(case_n)]
    for i in range(case_n):
        opt[i][i] = case_info[i]
    l = 0
    r = 1
    k = 1
    while k < case_n:
        while l < case_n-k:
            opt[l][r] = sum(case_info[l:r+1]) - min(opt[l+1][r], opt[l][r-1])
            l += 1
            r += 1
        l = 0
        r = k+1
        k += 1
        
    return opt[0][case_n-1]

    
for i in range(n):
    sc1 = compute(case_n[i],case_info[i])
    sc2 = sum(case_info[i]) - sc1
    print 'Case #%s: %s %s' % ((i+1), sc1, sc2)
    
'''
分析思路：动态规划 
考虑先手和后手在序列a(1); a(2);……; a(n)上博弈： 
  ① 如果先手取走了a1，那么问题转化成了两个人在a(2); a(3);……; a(n)上的博弈。 
  ② 如果先手取走an，就变成了在a(1); a(2);……; a(n-1)上的博弈。

于是，有了如下解题思路：
  可以定义f(L; R)为两个人在序列a(L); a(L+1);……; a(R)上博弈时，先手最多能拿到多少价值，
  那么此时后手拿到的价值一定为  sum(a[L:R]) - f(L; R)
  因为先后手的价值总和一定等于 sum(a[L:R]) 
  
现在思考一下：
  对于 R > L
  对于序列 a(L); a(L+1);……; a(R) 即序列a[L:R], 现在马贼A有两种选择：
   1. 马贼A拿a(L), 那么马贼B面对的序列就是 a[L+1:R]
       现在对于序列 a[L+1:R] ，马贼B就变成先手，马贼B的价值就是 f(L+1:R)
       所以马贼A在序列 a[L:R] 的价值就是 sum(a[L:R]) - f(L+1; R)
   2. 马贼A拿a(R), 那么马贼B面对的序列就是 a[L:R-1]
       现在对于序列 a[L:R-1] ，马贼B就变成先手，马贼B的价值就是 f(L:R-1)
       所以马贼A在序列 a[L:R] 的价值就是 sum(a[L:R]) - f(L; R-1)

    所以马贼A在序列 a[L:R] 中能获取的价值的动态转移方程就是：
        选a(L)： opt(L; R) = sum(a[L:R]) - f(L+1; R)
        选a(R)： opt(L; R) = sum(a[L:R]) - f(L; R-1)
    那么 opt(L; R) = max(sum(a[L:R]) - f(L+1; R), sum(a[L:R]) - f(L; R-1))
                   =  sum(a[L:R]) - min(f(L+1; R),f(L; R-1))

  对于初始条件：序列只有一个值 a[0], 那这个肯定被先手马贼A拿走，
      此时马贼A的价值 f(i; i) = a[i]
      
那就可以轻易的写出递推函数求解

def compute(case_i_info, l, r):
    if l == r:
        return case_i_info[l]
    if l < r:
        return sum(case_i_info[l:r+1])-min(compute(case_i_info, l+1, r), \
                   compute(case_i_info, l, r-1))

这样子时间复杂度太大，中间有许多重叠子问题
所以就需要用数组存放重叠子问题的解，降低时间复杂度

因为这里涉及两个指针 l 和 r
所以数组就是二维的：

新建一个数组 opt size为(case_n * case_n)
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

然后递归出口条件就是 f(i; i) = a[i]，所以opt对角线为 a[i]
[[4, 0, 0, 0, 0, 0],
 [0, 7, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0],
 [0, 0, 0, 9, 0, 0],
 [0, 0, 0, 0, 5, 0],
 [0, 0, 0, 0, 0, 2]]

然后根据状态转移方程
opt(L; R) =  sum(a[L:R]) - min(f(L+1; R),f(L; R-1))
可以得出结论：
opt[l][r] = sum(a[l:r+1]) - min(opt[l+1][r], opt[l][r-1])
即只需要计算opt右上角部分，因为opt是对称的矩阵
并且计算opt[i][j]时，只需要序列 a[i:j+1]的累加值 和 这个位置下边opt[i+1][j]和左边opt[i][j-1]这三个值
比如我计算 opt[0][1] = sum(a[0:2]) - min(opt[1][1], opt[0][0])

那么在遍历计算opt是有讲究了：
 需要从对角线往右上第一条斜线斜着遍历，然后再右上斜着遍历
比如：
第一次斜遍历：
[[4, 7, 0, 0, 0, 0],
 [0, 7, 7, 0, 0, 0],
 [0, 0, 2, 9, 0, 0],
 [0, 0, 0, 9, 9, 0],
 [0, 0, 0, 0, 5, 5],
 [0, 0, 0, 0, 0, 2]]
第二次斜遍历：
[[4, 7, 6, 0, 0, 0],
 [0, 7, 7, 11, 0, 0],
 [0, 0, 2, 9, 7, 0],
 [0, 0, 0, 9, 9, 11],
 [0, 0, 0, 0, 5, 5],
 [0, 0, 0, 0, 0, 2]]
第三次斜遍历：
[[4, 7, 6, 16, 0, 0],
 [0, 7, 7, 11, 16, 0],
 [0, 0, 2, 9, 7, 11],
 [0, 0, 0, 9, 9, 11],
 [0, 0, 0, 0, 5, 5],
 [0, 0, 0, 0, 0, 2]]
第四次斜遍历：
[[4, 7, 6, 16, 11, 0],
 [0, 7, 7, 11, 16, 14],
 [0, 0, 2, 9, 7, 11],
 [0, 0, 0, 9, 9, 11],
 [0, 0, 0, 0, 5, 5],
 [0, 0, 0, 0, 0, 2]]
第五次斜遍历：
[[4, 7, 6, 16, 11, 18],
 [0, 7, 7, 11, 16, 14],
 [0, 0, 2, 9, 7, 11],
 [0, 0, 0, 9, 9, 11],
 [0, 0, 0, 0, 5, 5],
 [0, 0, 0, 0, 0, 2]]

遍历之后：
opt右上角的值就是马贼A的最大价值

完
'''


#================================测试分割线=========================================
n = 2 
case_n = [6, 10] 
case_info = [[4, 7, 2, 9, 5, 2], [140, 649, 340, 982, 105, 86, 56, 610, 340, 879]]

def compute(case_i_info, l, r):
    if l == r:
        return case_i_info[l]
    if l < r:
        return sum(case_i_info[l:r+1])-min(compute(case_i_info, l+1, r), compute(case_i_info, l, r-1))
    
for i in range(n):
    sc1 = compute(case_info[i], 0, case_n[i]-1)
    sc2 = sum(case_info[i]) - sc1
    print 'Case #%s: %s %s' % ((i+1), sc1, sc2)
    
    
n = 2 
case_n = [6, 10] 
case_info = [[4, 7, 2, 9, 5, 2], [140, 649, 340, 982, 105, 86, 56, 610, 340, 879]]


def compute(case_n, case_info):
    
    opt = [[0]*case_n for i in range(case_n)]
    for i in range(case_n):
        opt[i][i] = case_info[i]
    l = 0
    r = 1
    k = 1
    while k < case_n:
        while l < case_n-k:
            opt[l][r] = sum(case_info[l:r+1]) - min(opt[l+1][r], opt[l][r-1])
            l += 1
            r += 1
        l = 0
        r = k+1
        k += 1
        
    return opt[0][case_n-1]


compute(case[0], case_info[0])
compute(case[1], case_info[1])
case_n = case[0]
case_info = case_info[0]
    




