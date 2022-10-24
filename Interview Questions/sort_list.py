# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sorted_list = []
        
        while head:
            sorted_list.append(head.val)
            head = head.next

        sorted_list = sorted(sorted_list)
        
        cur = dummy = ListNode()
        
        for element in sorted_list:
            cur.next = ListNode(val=element)
            cur = cur.next
            
        return dummy.next
        
        
        
