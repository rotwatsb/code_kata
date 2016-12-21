class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        l = []
        head = self
        while head:
            l.append(head.val)
            head = head.next
        return l

    def fromNum(self, n):
        node = ListNode(n % 10)
        if n >= 10:
            node.next = self.fromNum(n / 10)

    def __str__(self):
        return str(self.next:

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = int(''.join(l1.to_list()))
        b = int(''.join(l2.to_list()))
        ab = a + b
        ab_str = str(ab)
        return ' -> '.join(ab_str)
        
            
