# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        current = head
        while current.next:
            nodes.append(current)
            current = current.next
        nodes.append(current)
        m = len(nodes) - n
        if m - 1 >= 0 and m + 1 <= len(nodes) - 1:
            nodes[m-1].next = nodes[m+1]
        if m == 0:
            head = head.next
        if m == len(nodes) - 1:
            nodes[m-1].next = None    
        
        return head