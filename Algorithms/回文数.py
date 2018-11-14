# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:59:55 2018

@author: xiaohong
"""

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:   
            x_list = list(str(x))
            x_list.reverse()
            x_rev = ''.join(x_list)
            if x == int(x_rev):
                return True
            else:
                return False
        else:
            return False
        
        
        
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            x_list = list(str(x))
            
            if len(x_list) % 2 == 0:
                while len(x_list) > 0:
                    x_list_first = x_list.pop(0)
                    x_list_end = x_list.pop()
                    if x_list_first != x_list_end:
                        return False
                return True
            else:
                while len(x_list) > 1:
                    x_list_first = x_list.pop(0)
                    x_list_end = x_list.pop()
                    if x_list_first != x_list_end:
                        return False
                return True
            
isPalindrome(121)

'''
首先，我们应该处理一些临界情况。所有负数都不可能是回文，
例如：-123 不是回文，因为 - 不等于 3。所以我们可以对所有负数返回 false。

现在，让我们来考虑如何反转后半部分的数字。 
对于数字 1221，如果执行 1221 % 10，我们将得到最后一位数字 1，
要得到倒数第二位数字，我们可以先通过除以 10 把最后一位数字从 1221 中移除，
1221 / 10 = 122，再求出上一步结果除以10的余数，122 % 10 = 2，
就可以得到倒数第二位数字。如果我们把最后一位数字乘以10，再加上倒数第二位数字，
1 * 10 + 2 = 12，就得到了我们想要的反转后的数字。 
如果继续这个过程，我们将得到更多位数的反转数字。

现在的问题是，我们如何知道反转数字的位数已经达到原始数字位数的一半？

我们将原始数字除以 10，然后给反转后的数字乘上 10，
所以，当原始数字小于反转后的数字时，就意味着我们已经处理了一半位数的数字。
'''

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            x_char = str(x)
            rev_num = 1
            rev_char = ''
            half = False
            while not half:
                end1 = x % 10
                rem = x // 10
                rev_char = rev_char + str(end1)
                if rev_char !=  x_char[:rev_num]:
                    return False
                else:
                    rev_char_num = int(rev_char) * 10
                    x_char_sub = int(x_char) / 10.
                    if rev_char_num >= x_char_sub:
                        half = True
                rev_num += 1
                x = rem
            return True


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            for i in range(len(str(x))//2):
                if str(x)[i] != str(x)[-i-1]:
                    return False
            return True


'''
我的新做法：双指针对撞，将x每一位用列表存放起来，因为这样就可以切片查找
        并且数组是可变的，可以一直往后增长，字符不行，会内存溢出
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xlist = []
        while x > 0:
            res = x % 10
            x = x // 10
            xlist.append(res)
        
        left = 0
        right = len(xlist) - 1
        while left < right:
            if xlist[left] != xlist[right]:
                return False
            left += 1
            right -= 1
        return True



