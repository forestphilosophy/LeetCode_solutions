class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        current_l1 = l1    
        current_l2 = l2      
        carry = 0 
        
        result = ListNode()
        current_a = result

        while current_l1 or current_l2:
                    
            if current_l1.val + current_l2.val >= 10:
                current_a.val = (current_l1.val + current_l2.val + carry) % 10
                carry += 1
                        
            else:
                current_a.val = (current_l1.val + current_l2.val + carry)
                carry = 0 
            
            current_l1 = current_l1.next
            current_l2 = current_l2.next
            
            if current_l1:
                current_a.next = ListNode() 
                current_a = current_a.next 

        return result 
