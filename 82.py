from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
          return None
        answerHead = None
        current = head
        # find first Node with a unique value, make it answerHead
        if not head.next or (head.next and head.val != head.next.val):
          answerHead = head
        else:
          thisRunValue = current.val
          thisRunLength = 1
          while current and not answerHead:
            if not current.next:
              if thisRunLength == 1:
                answerHead = current
              else:
                return None
            else:
              if thisRunValue != current.next.val: # start new run
                if thisRunLength == 1:
                  answerHead = current
                else: # this run longer than 1
                  current = current.next
                  thisRunValue = current.val
                  thisRunLength = 1
              else: # this run still going
                current = current.next
                thisRunLength += 1
        # iterate through list dropping duplicate Nodes
        # current is last Node we are keeping
        # scout goes forward until we find the next Node we are keeping
        scout = current.next
        if scout:
          thisRunValue = scout.val
          thisRunLength = 1
        while scout:
          if not scout.next:
            if thisRunLength == 1:
              current.next = scout
            else:
              current.next = None # discard last run   
            scout = scout.next
          else: # there is a scout.next
            if thisRunValue != scout.next.val: # this run is ending
              if thisRunLength == 1:
                current.next = scout
                current = current.next
                scout = current.next
                thisRunValue = scout.val
              else: # this run should be discarded but we don't know about the next run yet
                scout = scout.next
                thisRunLength = 1
                thisRunValue = scout.val
            else: # this run is still going
              scout = scout.next
              thisRunLength += 1

        return answerHead

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
printList(answerHead)

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
printList(answerHead2)

inputHead3 = ListNode(1)
outputHead3 = ListNode(1)
answerHead3 = s.deleteDuplicates(inputHead3)
print(compareLists(outputHead3, answerHead3))
printList(answerHead3)
  
