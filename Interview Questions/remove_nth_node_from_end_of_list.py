# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def func(node):
            l = []
            while node:
                l.append(node.val)
                node = node.next
            return l

        l = func(head)

        l.pop(-n)
        
        if len(l) == 0:
            return None

        cur = dummy = ListNode()
        for i in l:
            cur.next = ListNode(i)
            cur = cur.next

        return dummy.next

