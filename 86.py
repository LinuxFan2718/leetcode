from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyLessThan = ListNode(-1)
        dummyGreaterThanOrEqualTo = ListNode(-1)
        lessThanCurrent = dummyLessThan
        greaterThanCurrent = dummyGreaterThanOrEqualTo
        current = head
        while current:
          print(current.val)
          if current.val < x:
            lessThanCurrent.next = ListNode(current.val)
            lessThanCurrent = lessThanCurrent.next
          else:
            greaterThanCurrent.next = ListNode(current.val)
            greaterThanCurrent = greaterThanCurrent.next
          current = current.next

        lessThanCurrent.next = dummyGreaterThanOrEqualTo.next
        if dummyLessThan.next:
          return dummyLessThan.next
        else:
          return dummyGreaterThanOrEqualTo.next

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

s = Solution()
x = 3
inputHead = ListNode(1)
values = [4,3,2,5,2]
current = inputHead
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

outputHead = ListNode(1)
values = [2,2,4,3,5]
current = outputHead
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

answerHead = s.partition(inputHead, x)
print(compareLists(outputHead, answerHead))
printList(answerHead)