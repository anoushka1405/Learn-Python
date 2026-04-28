'''
Uniform Cost Search (UCS):

- UCS is an uninformed search algorithm that expands the least-cost node first.
- It uses a priority queue to select nodes based on path cost g(n).
- UCS guarantees the optimal path for graphs with positive costs.
- Applications: Routing algorithms, path planning with costs.

'''

import heapq

# Sample weighted graph
graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}


def uniformCostSearch(start,goal):
    pq = [(0,start)] #Priority Queue : (total_cost,node)
    visited = set()

    while pq:
        cost,node = heapq.heappop(pq) #Popping node with lowest cost
        print(f"Visiting: {node} with cost {cost}")
        if(node==goal):
            print("Goal Found")
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor,weight in graph_weighted.get(node,[]):
                heapq.heappush(pq,(cost+weight,neighbor))
    return float('inf')


print("UCS Result:", uniformCostSearch('A', 'F'))
