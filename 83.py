from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
      dummy = ListNode(-1)
      dummy.next = head
      return dummy.next

s = Solution()
def compareLists(l1, l2):
  while True:
    if not l1 and not l2:
      return True
    if l1.val != l2.val:
      return False
    l1 = l1.next
    l2 = l2.next
    if not l1 and l2:
      return False
    if l1 and not l2:
      return False

def printList(l1):
  current = l1
  while current:
    if current.next:
      print(current.val, "->", end =" ")
    else:
      print(current.val)
    current = current.next

inputHead = ListNode(1)
values = [1, 2]
current = inputHead
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

outputHead = ListNode(1)
outputHead.next = ListNode(2)

answerHead = s.deleteDuplicates(inputHead)
print(compareLists(outputHead, answerHead))
printList(answerHead)

inputHead2 = ListNode(1)
values = [1, 2, 3, 3]
current = inputHead2
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

outputHead2 = ListNode(1)
outputHead2.next = ListNode(2)
outputHead2.next.next = ListNode(3)

answerHead2 = s.deleteDuplicates(inputHead2)
print(compareLists(outputHead2, answerHead2))
printList(answerHead2)

inputHead3 = ListNode(1)
outputHead3 = ListNode(1)
answerHead3 = s.deleteDuplicates(inputHead3)
print(compareLists(outputHead3, answerHead3))
printList(answerHead3)
  
