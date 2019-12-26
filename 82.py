from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        oldHead = head

        return oldHead

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

s = Solution()
inputHead = ListNode(1)
values = [2, 3, 3, 4, 4, 5]
current = inputHead
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

outputHead = ListNode(1)
values = [2, 5]
current = outputHead
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

answerHead = s.deleteDuplicates(inputHead)
print(compareLists(outputHead, answerHead))

inputHead2 = ListNode(1)
values = [1, 1, 2, 3]
current = inputHead2
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

outputHead2 = ListNode(2)
outputHead2.next = ListNode(3)

answerHead2 = s.deleteDuplicates(inputHead2)
print(compareLists(outputHead2, answerHead2))



  
