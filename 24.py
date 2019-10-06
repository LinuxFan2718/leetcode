from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
          return head
        oldHead = head
        newHead = head.next
        thirdNode = newHead.next
        head = newHead
        head.next = oldHead
        head.next.next = thirdNode

        current = oldHead
        while current and current.next and current.next.next:  
          oldFirst = current.next
          oldSecond = current.next.next
          third = oldSecond.next
          current.next = oldSecond
          oldSecond.next = oldFirst
          oldFirst.next = third
          current = oldFirst
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
printList(l1)
printList(s.swapPairs(l1))

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)
printList(l2)
printList(s.swapPairs(l2))