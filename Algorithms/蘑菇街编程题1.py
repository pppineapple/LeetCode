class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        cur = newhead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next    
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return newhead.next

def fun(list1, list2):
    l1 = ListNode(list1[0])
    cur1 = l1
    for i in range(1,len(list1)):
        cur1.next = ListNode(list1[i])
        cur1 = cur1.next
    
    l2 = ListNode(list2[0])
    cur2 = l2
    for j in range(1,len(list2)):
        cur2.next = ListNode(list2[j])
        cur2 = cur2.next
    
    s = Solution()
    newhead = s.mergeTwoLists(l1, l2)
    result = []
    while newhead:
        result.append(newhead.val)
        newhead = newhead.next
    
    return ' '.join(map(str, result))

while True:
    try:
        list1 = map(int, raw_input().split(' '))
        list2 = map(int, raw_input().split(' '))
        print fun(list1, list2)
    except:
        break