# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.solve(None, None, None, None, head, False)

    def solve(self, oddH, oddT, evenH, evenT, head, nextEven):
        if not head:
            if oddT:
                oddT.next = evenH
            return oddH if oddH else None
        else:
            nextElem = head.next
            head.next = None

        if not nextEven:
            if oddT:
                oddT.next = head
            return self.solve(oddH if oddH else head, head, evenH, evenT, nextElem, not nextEven)
        else:
            if evenT:
                evenT.next = head
            return self.solve(oddH, oddT, evenH if evenH else head, head, nextElem, not nextEven)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __init__(self, l):
        if len(l) > 1:
            self.val = l[0]
            self.next = ListNode(l[1:])
        else:
            self.val = l[0]
            self.next = None

    def __str__(self):
        return str(self.val) + (("->" + str(self.next)) if self.next else "")
        
