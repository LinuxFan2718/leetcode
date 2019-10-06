from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return head
            
def printList(l: ListNode) -> None:
  while l.next:
    print(l.val, " -> ", sep='', end='')
    l = l.next
  print(l.val)

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

s = Solution()
printList(s.swapPairs(l1))
