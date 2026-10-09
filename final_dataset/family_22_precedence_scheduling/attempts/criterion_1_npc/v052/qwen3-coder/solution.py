from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    # Topological sort with level tracking
    queue = deque()
    level = [0] * (n + 1)
    
    # Find all nodes with in-degree 0
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            level[i] = 1
    
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                level[neighbor] = level[node] + 1
    
    # Check if all nodes were processed (no cycles)
    if len(topo_order) != n:
        print("NO")
        return
    
    # Check if required levels exceed T
    max_level = max(level[1:])
    if max_level > T:
        print("NO")
        return
    
    # Group operations by level
    operations_by_level = defaultdict(list)
    for i in range(1, n + 1):
        operations_by_level[level[i]].append(i)
    
    # Check if any level has more operations than workstations
    for lvl in range(1, max_level + 1):
        if len(operations_by_level[lvl]) > M:
            print("NO")
            return
    
    # Output result
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = level[i]
    
    print("YES")
    print(*result[1:])

solve()