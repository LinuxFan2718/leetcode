from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        answer_head = ListNode(0)
        current_node = answer_head

        current_sum = l1.val + l2.val + carry
        carry = current_sum // 10
        ones_digit = current_sum % 10
        current_node.val = ones_digit
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            current_sum = l1.val + l2.val + carry
            carry = current_sum // 10
            ones_digit = current_sum % 10
            current_node.next = ListNode(ones_digit)
            current_node = current_node.next
            l1 = l1.next
            l2 = l2.next

        # both lists are empty
        if not l1 and not l2:
            if carry == 1:
                current_node.next = ListNode(carry)
            return answer_head

        # the other list is empty so can be ignored        
        remaining_digits = l1 if l1 else l2
        
        while remaining_digits and carry == 1:
            current_sum = remaining_digits.val + carry
            carry = current_sum // 10
            ones_digit = current_sum % 10
            current_node.next = ListNode(ones_digit)
            current_node = current_node.next
            remaining_digits = remaining_digits.next
        
        if not remaining_digits and carry == 1:
            current_node.next = ListNode(carry)
            return answer_head
        
        if remaining_digits and not carry == 1:
            current_node.next = remaining_digits
            return answer_head

        return answer_head

