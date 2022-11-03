# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def _len_node(self, head):
        _len = 1
        while head.next:
            head = head.next
            _len += 1
            
        return _len
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        len_node = self._len_node(head)
        
        if len_node % 2 == 0:
            target_idx = int(len_node / 2)
        
        elif len_node % 2 != 0:
            target_idx = int(len_node / 2)
            
        for i in range(target_idx):
            head = head.next
        
        return head
            
        
        
        
