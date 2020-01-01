from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        for _ in range(m-1):
          current = current.next
        previous = current
        nodesToReverse = []
        current = current.next
        for _ in range(n-m+1):
          nodesToReverse.append(current)
          current = current.next
        nodesToReverse.reverse()
        previous.next = nodesToReverse[0]
        i = 0
        for i in range(len(nodesToReverse) - 1):
          nodesToReverse[i].next = nodesToReverse[i+1]
        nodesToReverse[-1].next = current
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
m = 2
n = 4
inputHead = ListNode(1)
values = [2,3,4,5]
current = inputHead
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

outputHead = ListNode(1)
values = [4,3,2,5]
current = outputHead
for value in values:
  newCurrent = ListNode(value)
  current.next = newCurrent
  current = newCurrent

answerHead = s.reverseBetween(inputHead, m, n)
print(compareLists(outputHead, answerHead))
printList(answerHead)