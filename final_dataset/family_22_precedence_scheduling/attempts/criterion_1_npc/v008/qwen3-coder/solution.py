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
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # Level array to store the earliest time slot for each task
    level = [0] * (n + 1)
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            level[neighbor] = max(level[neighbor], level[node] + 1)
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all tasks can be scheduled within T time slots
    max_level = max(level[1:])
    if max_level >= T:
        print("NO")
        return
    
    # Count how many tasks are in each level
    level_count = [0] * T
    for i in range(1, n + 1):
        level_count[level[i]] += 1
    
    # Check if any level exceeds M stations
    for count in level_count:
        if count > M:
            print("NO")
            return
    
    # Output the result
    print("YES")
    print(*[level[i] + 1 for i in range(1, n + 1)])

solve()