'''
- A* is an informed search algorithm that uses heuristics to guide search.
- Node evaluation: f(n) = g(n) + h(n)
- g(n) = cost to reach node n
- h(n) = estimated cost from n to goal
- A* guarantees optimal solution if the heuristic is admissible (never overestimates).
- Applications: GPS navigation, AI game pathfinding.
'''
import heapq

# Sample weighted graph and heuristic values
graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
heuristic = {'A': 5, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 0}

# A* Search Algorithm

def a_star_search(start, goal):
    pq = [(heuristic[start], 0, start)]  # (f = g + h, g, node)
    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)  # Pop node with lowest f
        print(f"Visiting: {node}, g={g}, f={f}")
        if node == goal:
            print("Goal found!")
            return g
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph_weighted.get(node, []):
                heapq.heappush(pq, (g + cost + heuristic[neighbor], g + cost, neighbor))
    return float('inf')

'''
- Iterative Deepening A (IDA):**
- IDA* is a memory-efficient variant of A*.
- Performs depth-first search iteratively, increasing the f-cost threshold each iteration.
- Combines advantages of DFS (low memory) and A* (heuristic guidance).
- Applications: Large search spaces, puzzle solving (like 15-puzzle).

'''

def ida_star(start, goal):
    def dfs(path, g, threshold):
        node = path[-1]
        f = g + heuristic[node]  # f = g + h
        if f > threshold:
            return f
        print(f"Visiting: {node}, g={g}, f={f}, threshold={threshold}")
        if node == goal:
            print("Goal found!")
            return 'FOUND'
        min_threshold = float('inf')
        for neighbor, cost in graph_weighted.get(node, []):
            if neighbor not in path:
                t = dfs(path + [neighbor], g + cost, threshold)
                if t == 'FOUND':
                    return 'FOUND'
                if t < min_threshold:
                    min_threshold = t
        return min_threshold

    threshold = heuristic[start]
    while True:
        temp = dfs([start], 0, threshold)
        if temp == 'FOUND':
            return threshold
        if temp == float('inf'):
            return float('inf')
        threshold = temp


print("A* Result:", a_star_search('A', 'F'))
print("IDA* Result:", ida_star('A', 'F'))
