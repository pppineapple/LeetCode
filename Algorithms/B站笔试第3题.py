#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:29:04 2018

@author: pineapple
"""

'''
B站笔试第３题：计算字符串形式的四则运算，不带括弧
'7+3*4*5+2+4-3-1'
'2-3*1'
利用栈的性质先算乘除，再算加减
注意将字符串转化为列表，因为字符串操作10会拆开成1和0
'''

def compute(a):
    sy = '+-*/'
    alist = []
    i = 0
    while i < len(a):
        asub = ''
        if a[i] in sy:
            asub += a[i]
            i += 1
        else:
            while i < len(a) and a[i] not in sy:
                asub += a[i]
                i += 1
        alist.append(asub)
    
    
    stack = []
    symbol1 = '+-'
    symbol2 = '*/'
    i = 0
    while i < len(alist):
        if alist[i].isdigit():
            stack.append(int(alist[i]))
            i += 1
        elif alist[i] in symbol1:
            stack.append(alist[i])
            i += 1
        elif alist[i] in symbol2:
            num1 = stack.pop()
            num2 = int(alist[i+1])
            if alist[i] == '*':
                result = num1 * num2
            elif alist[i] == '/':
                result = num1 / num2
            stack.append(result)
            i += 2    
    stack.reverse()
            
    while len(stack) > 1:
        number1 = stack.pop()
        s = stack.pop()
        number2 = stack.pop()
        if s == '+':
            result = number1 + number2
        elif s == '-':
            result = number1 - number2
        stack.append(result)
    return stack[0]


while True:
    try:
        a = []
        stop = False
        while not stop:
            i = raw_input().split()[0]
            if i == 'END':
                stop = True
            else:
                a.append(i)
        for p in a:
            print compute(p)
    except:
		break