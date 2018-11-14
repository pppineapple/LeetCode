

'''
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。
'''

'''
我的：时间复杂度O(n), 空间复杂度O(1)
思路：直接根据他的三个条件写出判断语句
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True

        if word[0].islower():
            for i in word[1:]:
                if not i.islower():
                    return False
            return True
        else:
            second = word[1]
            point = 2
            while point < len(word):
                if (second.islower() and word[point].islower()) or \
                   (second.islower() is False and word[point].islower() is False):
                    pass
                else:
                    return False
                point += 1

            return True

    '''
    更简洁的代码
    '''

    class Solution(object):
        def detectCapitalUse(self, word):
            """
            :type word: str
            :rtype: bool
            """
            if word == word.upper():
                return True
            if word == word.lower():
                return True

            if word[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and word[1:] == word.lower()[1:]:
                return True
            else:
                return False