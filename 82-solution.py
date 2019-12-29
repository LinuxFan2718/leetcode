from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28336/Python-in-place-solution-with-dummy-head-node.
class Solution:
  def deleteDuplicates(self, head):
    dummy = pre = ListNode(0)
    # pre is the rightmost known good Node
    # in my solution, pre is current, current is scout
    current = head
    dummy.next = head
    while current and current.next:
        if current.val == current.next.val:
            while current and current.next and current.val == current.next.val:
                current = current.next # go forward while node values are equal
            current = current.next
            pre.next = current
        else:
            pre = pre.next
            current = current.next
    return dummy.next


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
  
