#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 08:20:58 2018

@author: pineapple
"""

'''

给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。
示例 1：
输入：S = "5F3Z-2e-9-w", K = 4
输出："5F3Z-2E9W"
解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     注意，两个额外的破折号需要删掉。
     
示例 2：
输入：S = "2-5g-3-J", K = 2

输出："2-5G-3J"
解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，
第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
'''

'''
我的：　时间复杂度O(n) 空间复杂度O(1)
思路：这道题目的意思是第一项可以是任意长度，但是后面的项必须满足K长度
    所以就是判断在第一项字符数是多长的时候，总长度减去第一个字符的长度
    之后可以安K长度平分开．
'''
  

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        slist = S.replace('-','')
        point = 0
        while (len(slist) - point) % K != 0:
            point += 1
        result = []
        if point == 0:            
            for j in range(1,len(slist)+1):
                if j%K==0:
                    result.append(slist[j-K:j])
        else:
            result.append(slist[:point])
            for j in range(point+1, len(slist)+1):
                if (j-point)%K == 0:
                    result.append(slist[j-K:j])
        return ('-'.join(result)).upper()

S = "5F3Z-2e-9-w"
K = 4
S = "2-5g-3-J"
K = 2
S = "2-4A0r7-4k"
K = 4
S="2-4A0r7-4k"
K=3
solution = Solution()
solution.licenseKeyFormatting(S,K)
                