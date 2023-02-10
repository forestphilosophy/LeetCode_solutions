# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_l = []
        l2_l = []

        while l1:
            l1_l.append(l1.val)

            l1 = l1.next

        while l2:
            l2_l.append(l2.val)

            l2 = l2.next      

        num1 = int(''.join(str(i) for i in l1_l)[::-1])
        num2 = int(''.join(str(i) for i in l2_l)[::-1])

        res_num_str = str(num1+num2)[::-1]
        res_num = int(res_num_str)

        if len(res_num_str) == 1:
            return ListNode(res_num)

        cur = dummy = ListNode(0)
        for e in res_num_str:
            cur.next = ListNode(e)
            cur = cur.next

        return dummy.next




