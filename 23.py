from typing import List
from bisect import bisect
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def firstElement(self, x):
        return x[1]

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [list for list in lists if list != None]
        if len(lists) == 0:
          return None
        rawValues = [(i, x.val) for i, x in enumerate(lists)] #(index, value)
        sortedTuples = sorted(rawValues, key=self.firstElement)
        tupleToAdd = sortedTuples.pop(0) #(index, value)
        # sorted tuples is still sorted by value
        nodeToAdd = lists[tupleToAdd[0]]
        if nodeToAdd.next:
          indexOfLists = tupleToAdd[0]
          lists[indexOfLists] = nodeToAdd.next
          valueOfNewNode = lists[indexOfLists].val
          # sortedTuples is out of date now
          # need to add this new element
          indexOfSortedTuples = bisect([x[1] for x in sortedTuples] , valueOfNewNode)
          sortedTuples.insert(indexOfSortedTuples, (indexOfLists, valueOfNewNode))
          # sortedTuples is sorted again
        elif nodeToAdd.next == None:
          indexOfLists = tupleToAdd[0]
          del lists[indexOfLists]
          sortedTuples = [(i, x) if i < indexOfLists else (i-1, x) for i, x in sortedTuples]
        head = nodeToAdd
        current = head
        while len(lists) > 0:
          tupleToAdd = sortedTuples.pop(0) #(index, value)
          # sorted values is still sorted by value
          nodeToAdd = lists[tupleToAdd[0]]
          if nodeToAdd.next:
            indexOfLists = tupleToAdd[0]
            lists[indexOfLists] = nodeToAdd.next
            valueOfNewNode = lists[indexOfLists].val
            # sortedTuples is out of date now
            # need to add this new element
            indexOfSortedTuples = bisect([x[1] for x in sortedTuples] , valueOfNewNode)
            sortedTuples.insert(indexOfSortedTuples, (indexOfLists, valueOfNewNode))
            # sortedTuples is sorted again
          elif nodeToAdd.next == None:
            indexOfLists = tupleToAdd[0]
            del lists[indexOfLists]
            sortedTuples = [(i, x) if i < indexOfLists else (i-1, x) for i, x in sortedTuples]
          current.next = nodeToAdd
          current = current.next
        return head
            
def printList(l: ListNode) -> None:
  while l:
    print(l.val, "->")
    l = l.next

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1,l2,l3]
s = Solution()
printList(s.mergeKLists(lists))
