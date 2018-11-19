'''
给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

示例 1:

输入: [3, 1, 4, 1, 5], k = 2
输出: 2
解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。
示例 2:

输入:[1, 2, 3, 4, 5], k = 1
输出: 4
解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
示例 3:

输入: [1, 3, 1, 5, 4], k = 0
输出: 1
解释: 数组中只有一个 0-diff 数对，(1, 1)。
注意:

数对 (i, j) 和数对 (j, i) 被算作同一数对。
数组的长度不超过10,000。
所有输入的整数的范围在 [-1e7, 1e7]。
'''


'''
我的：时间复杂度O(n) 空间复杂度O(n)
思路：根据题意：是要在数组里面找数队，数对要符合差是k的条件，最后输出不重复的数对的个数
    因为题目有说数对 (i, j) 和数对 (j, i) 被算作同一数对。所以可以直接考虑（i，j）并且i<j,从而就不考虑k<0的情况了
    如果k > 0,那只需要遍历set(nums),然后看 （i + k）是否在set(nums)里面就可以了
    如果k == 0,呢只要统计数组nums中有哪些重复的项可以了
'''

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k == 0:
            hash = {}
            for i in nums:
                hash[i] = hash.get(i, 0) + 1
            return sum(hash[i] > 1 for i in hash)
        elif k > 0:
            ans = 0
            distinct_nums = set(nums)
            for i in distinct_nums:
                if i + k in distinct_nums:
                    ans += 1
            return ans

