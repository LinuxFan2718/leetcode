# linked list head is most recently used element
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.hash = {}

    def get(self, key: int) -> int:
        if key in self.hash.keys():
          this_node = self.hash[key]
          # remove this node from where it is
          this_left = this_node.left
          this_right = this_node.right
          if this_left:
            this_left.right = this_right
          if this_right:
            this_right.left = this_left
          # move this node to head
          old_head = self.head
          self.head = this_node
          self.head.right = old_head
          old_head.left = self.head

          return this_node.val[1]
        else:
          return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.hash.keys():
          return
        else:
          if len(self.hash) == self.capacity:
            node_to_remove = self.tail
            self.tail = node_to_remove.left
            node_to_remove.left.right = None
            key_to_remove = node_to_remove.val[0]``
            del self.hash[key_to_remove]
            del node_to_remove
          
          new_node = Node((key, value))
          self.hash[key] = new_node
          if self.head != None:
            old_head = self.head
            self.head = new_node
            self.head.right = old_head
          else:
            self.head = new_node
          return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)

# cache.put(1, 1)
# cache.put(2, 2)
# a1 = cache.get(1)
# print(a1, a1 == 1)
# pass
# cache.put(3, 3) # evicts key 2
# a2 = cache.get(2)
# print(a2, a2 == -1)
# cache.put(4, 4)
# a3 = cache.get(1)
# print(a3, a3 == -1)
# a4 = cache.get(3)
# print(a4, a4 == 3)
# a5 = cache.get(4)
# print(a5, a5 == 4)
# print()
c2 = LRUCache(1)
c2.put(2,1)
a1 = c2.get(2)
print(a1, a1 == 1)
c2.put(3,2) # pushes out 2
a2 = c2.get(2)
print(a2, a2 == -1)
a3 = c2.get(3)
print(a3, a3 == 2)

["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
