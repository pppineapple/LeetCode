# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:13:53 2018

@author: xiaohong
"""

'''

给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，
其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
'''


'''
我的 超时  时间复杂度 O(n^3)
思路： 遍历
'''
def numberOfBoomerangs(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dis(p1, p2):
            return (p1[0]-p2[0]) **2 + (p1[1]-p2[1]) ** 2
        
        count = 0
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                for k, p3 in enumerate(points):
                    if dist(p1,p2) == dist(p1,p3) and i!=j!=k:
                        count += 1
        return count

'''
别人 0.68 时间复杂度 O(n^2)
思路： 先固定一个点p1，然后遍历其他点，统计其他点到p1的距离，将这个距离存入字典record中，
        字典的value为与点p1距离为key的点的个数,
        然后对字典进行遍历，将value大于等于2即表明其他到p1的距离相等的点的个数，
        然后计算这些点两两的组合数，用组合数公式 C2n = n*(n-1)
        最后累加这些组合数即可
        
'''

def numberOfBoomerangs(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dist(p1, p2):
            return (p1[0]-p2[0]) **2 + (p1[1]-p2[1]) ** 2
        
        count = 0
        for i, p1 in enumerate(points):
            record = {}
            for j, p2 in enumerate(points):
                if i!=j:
                    d = dist(p1,p2)
                    record[d] = record.get(d,0) + 1 #字典的get方法会放回key对应的键值，如果key对应的键值不存在，会返回第二个参数
            
            for p in record:
                if record[p] >= 2:
                     count += record[p] * (record[p]-1)   
                     
        return count
        
'''
第二次做的代码
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in points:
            i_dist = {}
            for j in points:
                dij = (i[0]-j[0])**2 + (i[1]-j[1])**2
                if dij > 0:
                    i_dist[dij] = i_dist.get(dij, 0) + 1
            
            for k in i_dist:
                if i_dist[k] > 1:
                    result += i_dist[k]*(i_dist[k]-1)
        return result
    
points = [[0,0],[1,0],[2,0]]
s = Solution()
s.numberOfBoomerangs(points)


