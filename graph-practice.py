"""
problem 1 best solution. really good, helper function makes it easier.

problem 2 algo right. just had that last bug in the end

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have a common ancestor of 4.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

has_common_ancestor(parent_child_pairs_1, 3, 8) => false
has_common_ancestor(parent_child_pairs_1, 5, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 9) => true
has_common_ancestor(parent_child_pairs_1, 1, 3) => false
has_common_ancestor(parent_child_pairs_1, 3, 1) => false
has_common_ancestor(parent_child_pairs_1, 7, 11) => true
has_common_ancestor(parent_child_pairs_1, 6, 5) => true
has_common_ancestor(parent_child_pairs_1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parent_child_pairs_2 = [
    (11, 10), (11, 12), (2, 3), (10, 2), (10, 5), 
    (1, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

has_common_ancestor(parent_child_pairs_2, 4, 12) => true
has_common_ancestor(parent_child_pairs_2, 1, 6) => false
has_common_ancestor(parent_child_pairs_2, 1, 12) => false

n: number of pairs in the input

"""
# Question 2
parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

parent_child_pairs_2 = [
    (11, 10), (11, 12), (2, 3), (10, 2), (10, 5),
    (1, 3), (3, 4), (5, 6), (5, 7), (7, 8)
]

def has_common_ancestor(parent_child_pairs_2, node1, node2):
    parent_child_pairs_2 = sorted(parent_child_pairs_2, key= lambda x: x[1])
    ancestors1 = [parent for parent, child in parent_child_pairs_2 if child == node1]
    ancestors2 = [parent for parent, child in parent_child_pairs_2 if child == node2]
    common = set(ancestors1).intersection(ancestors2)
    if len(common) > 0:
        return True
    keep_going = True
    while keep_going:
        these_parents1 = []
        these_parents2 = []
        for ancestor in ancestors1:
            these_parents1 = [parent for parent, child in parent_child_pairs_2 if child == ancestor]
        
        for ancestor in ancestors2:
            these_parents2 = [parent for parent, child in parent_child_pairs_2 if child == ancestor]
            
        ancestors1.extend(these_parents1)
        ancestors2.extend(these_parents2)
        common = set(ancestors1).intersection(ancestors2)
        if len(common) > 0:
            return True
        if len(these_parents1) + len(these_parents2) == 0:
            return False
    
            
        
            
            
print(has_common_ancestor(parent_child_pairs_2, 6, 7))
                
print(has_common_ancestor(parent_child_pairs_2, 6, 8))
print(has_common_ancestor(parent_child_pairs_2, 1, 8))
print()
    
print(has_common_ancestor(parent_child_pairs_1, 3, 8))
print(has_common_ancestor(parent_child_pairs_1, 5, 8))
print(has_common_ancestor(parent_child_pairs_1, 6, 8))
print(has_common_ancestor(parent_child_pairs_1, 6, 9))
print(has_common_ancestor(parent_child_pairs_1, 1, 3))
print(has_common_ancestor(parent_child_pairs_1, 3, 1))
print(has_common_ancestor(parent_child_pairs_1, 7, 11))
print(has_common_ancestor(parent_child_pairs_1, 6, 5))
print(has_common_ancestor(parent_child_pairs_1, 5, 6))
print(has_common_ancestor(parent_child_pairs_2, 4, 12))
print(has_common_ancestor(parent_child_pairs_2, 1, 6))
print(has_common_ancestor(parent_child_pairs_2, 1, 12))





# Question 1

parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]

def helper(d, match):
    answer = []
    for key, value in d.items():
        if value == match:
            answer.append(key)
    return answer

def find_nodes_with_zero_and_one_parents(parent_child_pairs):
    child_num_parents_hash = {}
    for pair in parent_child_pairs:
        child_num_parents_hash[pair[0]] = 0
        child_num_parents_hash[pair[1]] = 0
    for parent_child_pair in parent_child_pairs:
        parent = parent_child_pair[0]
        child = parent_child_pair[1]
        if child in child_num_parents_hash.keys():
            child_num_parents_hash[child] += 1

    individuals_with_zero_parents = helper(child_num_parents_hash, 0)
    individuals_with_one_parent = helper(child_num_parents_hash, 1)
    return individuals_with_zero_parents, individuals_with_one_parent

ans1 = find_nodes_with_zero_and_one_parents(parent_child_pairs)
# print(ans1)
# print(ans1[0], ans1[0] == [1, 2, 4])
# print(ans1[1], ans1[1] == [5, 7, 8, 9, 11])

print()