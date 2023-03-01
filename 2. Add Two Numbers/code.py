# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        res = root
        carry = 0
        while(l1 or l2):
            print(carry)
            if(l1):
                res.val += l1.val
                l1 = l1.next
            print(carry, "After l1", res.val)
            if(l2):
                res.val += l2.val
                l2 = l2.next
            res.val += carry
            carry = res.val // 10
            if res.val > 9:
                res.val = res.val % 10
            if l1 or l2:
                res.next = ListNode()
                res = res.next
        if carry:
            res.next = ListNode(carry)
            res = res.next
        return root