from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        current = head
        for _ in range(k):
          if current == None:
            return head
          current = current.next

        nodes = []
        current = head
        for _ in range(k):
          nodes.append(current)
          current = current.next
        nodes.reverse()
        head = nodes[0]
        lastNode = nodes[0].next
        for i in range(k - 1):
          nodes[i].next = nodes[i + 1]
        nodes[k - 1].next = lastNode
        finalNode = nodes[k - 1]

        while True:
          current = lastNode
          for _ in range(k):
            if current == None:
              return head
            current = current.next
          nodes = []
          current = lastNode
          for _ in range(k):
            nodes.append(current)
            current = current.next
          nodes.reverse()
          finalNode.next = nodes[0]

          lastNode = nodes[0].next
          for i in range(k - 1):
            nodes[i].next = nodes[i + 1]
          nodes[k - 1].next = lastNode
          finalNode = nodes[k - 1]
            
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
printList(s.reverseKGroup(l1,2))

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)
printList(l2)
printList(s.reverseKGroup(l2, 2))

l3 = ListNode(1)
l3.next = ListNode(2)
l3.next.next = ListNode(3)
l3.next.next.next = ListNode(4)
l3.next.next.next.next = ListNode(5)
printList(l3)
printList(s.reverseKGroup(l3, 3))