
def tree_ref(tree, index):
    if not index:
        return tree
    return tree_ref(tree[index[0]], index[1:])

# Test cases
tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))

print(tree_ref(tree, (3, 1))) 
print(tree_ref(tree, (1, 1, 1)))  
print(tree_ref(tree, (0,)))  
print(tree_ref(tree, (0, 0, 1)))


