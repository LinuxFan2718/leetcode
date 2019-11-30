from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
          return None
        listOfNodes = []
        current = head
        while current != None:
          listOfNodes.append(current)
          current = current.next
        k = k % len(listOfNodes)
        newHeadIndex = (len(listOfNodes) - k) % len(listOfNodes)
        newHead = listOfNodes[newHeadIndex]
        listOfNodes[-1].next = head
        listOfNodes[newHeadIndex-1].next = None
        return newHead

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = None
k = 2
ans = s.rotateRight(head, k)
current = ans
for num in [4, 5, 1, 2, 3]:
  print(current.val == num, current.val, num)
  current = current.next
print(current == None, current)

head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
k = 4
ans2 = s.rotateRight(head2, k)
current2 = ans2
for num in [2, 0, 1]:
  print(current2.val == num, current2.val, num)
  current2 = current2.next
print(current2 == None, current2)

head3 = None
k = 0
ans3 = s.rotateRight(head3, k)

head4 = ListNode(1)
head4.next = ListNode(2)
k = 0
ans4 = s.rotateRight(head4, k)
current4 = ans4
for num in [1,2]:
  print(current4.val == num, current4.val, num)
  current4 = current4.next
print(current4 == None, current4)
