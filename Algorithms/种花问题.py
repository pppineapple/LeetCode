# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 08:11:43 2018

@author: xiaohong
"""

'''
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），
和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。


示例 1:
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
'''

'''
我的 0.96
思路 将flowerbed(1-0)数组转化为含1索引列表，然后用数学表达式判断
'''

def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        f_index = [i for i in range(len(flowerbed)) if flowerbed[i]==1]
        if len(f_index) == 0 and len(flowerbed) <= 2:
            return 1 >= n
        elif len(f_index) == 0 and len(flowerbed) > 2:
            f_n = 2 + (len(flowerbed)-2)//3
            return f_n >= n
            
        if len(f_index) == 1:
            f_n = f_index[0]//2 + (len(flowerbed)-1-f_index[0])//2
            return  f_n >= n
        f_n = 0
        for j in range(len(f_index)):
            if j == 0:
                f_n += f_index[j] // 2
            else:
                if f_index[j]-f_index[j-1] > 3:
                    f_n += (f_index[j]-f_index[j-1])//3
            if j == len(f_index)-1:
                f_n += (len(flowerbed)-1-f_index[j])//2
                            
        return f_n >= n

'''
比人 更优雅 1
思路： 遍历数组，然后判断当前位置，前位置，后位置有没有种花
        然后根据不同的情况进行跳跃
        在列表头位置和尾位置巧妙的用or条件来连接
'''

def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
    
        i = 0
        count = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0: # 当前没花
                if i-1<0 or flowerbed[i-1] == 0: #判断前一个位置没花
                    if i+1>=len(flowerbed) or flowerbed[i+1] == 0: #判断后一个位置没花
                        count += 1
                        if count == n:
                            return True
                        i += 2
                    else:
                        i += 3
                else:
                    i += 1
            else:
                i += 2
        return False
                    
                
        
        
        
        