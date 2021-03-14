#Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        prev = ListNode(0,head)
        previous_node = prev
        
        while current:
    
            if current.val == previous_node.val:
                previous_node.next = current.next
                    
            previous_node = current      
            current = current.next
        
        return prev.next
        
 #Solution 2       
 class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        current = head.next
        prev = head
        
        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        
        return head
