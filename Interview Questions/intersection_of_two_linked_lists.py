# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def len_link(self,listnode):
        count=0
        while(listnode):
            count+=1
            listnode=listnode.next
        return count
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.len_link(headA)
        lenB = self.len_link(headB)
        
        nodeA = headA
        nodeB = headB
        if lenA > lenB:
            diff = lenA - lenB
            for i in range(diff):
                nodeA = nodeA.next

        elif lenA < lenB:
            diff = lenB - lenA
            for i in range(diff):
                nodeB = nodeB.next
        
        if nodeA == nodeB:
            return nodeA
        
        for i in range(lenA):
            if nodeA.next:
                if nodeA.next == nodeB.next:
                    return nodeA.next
                else:
                    nodeA = nodeA.next
                    nodeB = nodeB.next
                
        return None

        

            
