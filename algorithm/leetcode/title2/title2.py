# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        p, bone, carry = l1, True, 0        
        while l1 and l2:
            l1.val = l1.val + l2.val + carry
            carry = l1.val // 10
            l1.val = l1.val % 10
            if l1.next:
                pass
            elif l2.next:
                l1.next, l2.next = l2.next, None
            elif carry > 0:
                l1.next = ListNode(carry)
                carry = 0
            if carry > 0 and l2.next == None:
                l2.next = ListNode(carry)
                carry = 0
            l1, l2 = l1.next, l2.next
        return p