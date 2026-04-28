'''
Depth Limited Search

- DLS is a variant of DFS with a maximum depth limit.
- Prevents infinite loops in infinite graphs.
- Useful for iterative deepening search.
- Limitation: May miss the goal if it’s beyond the depth limit.

'''

# Sample graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def depth_limited_search(node,goal,limit):
    print("Visiting Node : ",node,"\nLimit Remaining : ",limit)
    if node==goal:
        print("Goal Found!")
        return True
    if limit<=0:
        return False
    
    for child in graph.get(node,[]):
        if depth_limited_search(child,goal,limit-1):
            return True
        
    return False
    

print("DLS Result (limit=2):", depth_limited_search('A', 'F', 2))
print("DLS Result (limit=3):", depth_limited_search('A', 'F', 3))
  

