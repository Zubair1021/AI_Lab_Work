def depth(expr):
    if not isinstance(expr, (list, tuple)):
        return 0
    max_depth = 0
    for item in expr:
        max_depth = max(max_depth, depth(item))
    return max_depth + 1

# Test cases
print("Depth is :",depth('x')) 
#print("Depth is :",depth(('expt', 'x', 2)))  
#print("Depth is :",depth(('+', ('expt', 'x', 2), ('expt', 'y', 2)))) 
#print("Depth is :",depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))  
