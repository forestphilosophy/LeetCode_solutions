class Solution(object):
    def mergeTwoLists(self, l1, l2):
        merged_list = ListNode()  
        current = merged_list  
        
        while l1 and l2:  
            
            if l1.val < l2.val:  
                current.next = l1  
                l1 = l1.next  
                
            else:  
                current.next = l2  
                l2 = l2.next  
                
            current = current.next  
            
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
  
        return merged_list.next
