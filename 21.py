from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        if l1 == None:
          return l2
        if l2 == None:
          return l1
        if l1.val > l2.val:
          temp = l1 # swap so l1 has smaller first element
          l1 = l2
          l2 = temp
        head = l1
        while l1.next and l2.next:
          if l1.next.val < l2.val:
            l1 = l1.next
          elif l1.next.val >= l2.val:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l2 = temp2
        if l1.next == None:
          l1.next = l2 # to get here we know that l1.val < l2.val
        elif l2.next == None:
          while l1.next and l1.next.val < l2.val:
            l1 = l1.next
          temp1 = l1.next
          temp2 = l2.next
          l1.next = l2
          l2.next = temp1
          l2 = temp2         
        return head


def printList(l: ListNode) -> None:
  while l:
    print(l.val, "->")
    l = l.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

s = Solution()
printList(s.mergeTwoLists(l1, l2))