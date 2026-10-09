from collections import defaultdict, deque

def topological_sort(n, edges):
    # Build adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1
    
    # Find all nodes with in-degree 0
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Remove this node and update in-degrees
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we processed all nodes, return the order; otherwise there's a cycle
    if len(result) == n:
        return result
    else:
        return None

# Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

# Perform topological sort
order = topological_sort(n, edges)

# Output result
if order:
    print("YES")
    print(" ".join(map(str, order)))
else:
    print("NO")