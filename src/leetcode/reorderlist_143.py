# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        a = head
        if not a:
            return a
        b = head

        pref = None
        pref_size = 0
        while(a and b):
            (c, b, adv2) = self.adv(a, b)
            a.next = pref
            pref = a
            a = c
            pref_size += 1

        (a, b) = (a, pref) if adv2 else (pref, a)
        pref = None
        while(a and b):
            (c, d) = (a.next, b.next)
            a.next = pref
            pref = a
            b.next = pref
            pref = b
            a = c
            b = d

        if a:
            a.next = pref
            pref = a

    def adv(self, a, b):
        a = a.next
        b = b.next
        if not b:
            return (a, b, False)
        else:
            b = b.next
            return (a, b, True)

        
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
        
