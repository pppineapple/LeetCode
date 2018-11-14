'''
给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。

示例 :

输入: "aba", "cdc"
输出: 3
解析: 最长特殊序列可为 "aba" (或 "cdc")
说明:

两个字符串长度均小于100。
字符串中的字符仅含有 'a'~'z'。
'''


'''
别人的：时间复杂度O(1) 空间复杂度O(1)
思路：最开始看这个题，半天没看懂，然后看了其他人的思路。
    这个题度意思是：在两个字符串中，找到一个最长的子字符串，这个字符串不是另外一个字符串的子字符串，这个子字符串不一定是连续的
    所以可以这样思考，假设有两个要比较的字符串 a,b
    如果 len(a) == len(b):
        如果 a == b ，那么说明a的任意子字符串都可以在b中找到，所以返回 -1
        如果 a != b , 那么说明a就不可以用b的子字符串表示，所以就返回a的长度
    如果 len(a) != len(b):
        那字符串长度大的那个就不能被长度小的那个字符串表示，所以就返回字符串长达大的那个字符串的长度
'''
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: st
        :rtype: int
        """
        if len(a) == len(b) and a == b:
            return -1
        else:
            return max(len(a), len(b))