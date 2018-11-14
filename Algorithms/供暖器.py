# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 14:02:47 2018

@author: xiaohong
"""

'''
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。

所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

说明:

给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。
示例 1:

输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
'''


'''
别人的： 时间复杂度O(nlogm) 空间复杂度O(1)
思路：
先将取暖器数组排序，在遍历所有house，
对每个house，在取暖器数组中进行binary search，
如果命中，则说明取暖器位置和house位置重合，
这个house的最小半径为0；
如果没有命中，则使用返回的index，
将index左边和右边的取暖器坐标与house坐标求差值，找出这个house最小半径。
说白了，也是在查找house的最近左右取暖器。
'''



def findRadius(houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        heaters.sort()
        if len(heaters) == 1:
            return max(heaters[0]-houses[0], houses[-1]-heaters[0])
                
        maxr = 0
        for h in houses:            
            start = 0
            end = len(heaters)-1
            mid = (end+start) // 2
            if h <= heaters[start]:
                new_maxr = heaters[start] - h

            elif h >= heaters[end]:
                new_maxr = h - heaters[end]

            else:
                found = False
                while end > start+1  and not found:
                    if h == heaters[mid]:
                        new_maxr = 0
                        found = True
                    else:
                        if h > heaters[mid]:
                            start = mid 
                        else:
                            end = mid 
                    mid = (end+start)//2
                if not found:
                    new_maxr = min(h-heaters[start], heaters[end]-h)
                    print new_maxr

            maxr = max(maxr, new_maxr)
        return maxr
         
houses = [1,2,3]
heaters = [2]

houses = [1,2,3,4]
heaters = [1,4]


houses = [1]
heaters = [1,2,3,4]

houses = [1,2,3,5,15]
heaters = [2,30]

houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
'161834419'
findRadius(houses, heaters)
findRadius([1,2,3],[2])
h =   282475249
h = houses[1]
h = 2        
h = 3          
h = 15        
            
            
            
            
            
            
            
            
            
            
            
            