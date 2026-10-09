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
    
    # Kahn's algorithm with level tracking
    # Queue stores (node, level) where level is the cycle number
    queue = deque()
    cycle = [0] * (n + 1)
    
    # Find all nodes with in-degree 0
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append((i, 1))
    
    processed = 0
    
    while queue:
        # Group nodes by their cycle number to respect capacity M
        current_cycle = queue[0][1] if queue else 1
        cycle_count = 0
        temp_nodes = []
        
        # Collect all nodes that should be scheduled in current_cycle
        while queue and queue[0][1] == current_cycle and cycle_count < M:
            node, level = queue.popleft()
            if level > T:
                print("NO")
                return
            cycle[node] = level
            processed += 1
            cycle_count += 1
            
            # Add neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    temp_nodes.append((neighbor, level + 1))
        
        # Put back remaining nodes in this cycle if any
        for item in temp_nodes:
            queue.append(item)
            
        # If we couldn't place any nodes in this iteration but there are still nodes,
        # it means we exceeded the capacity M for some cycle
        if cycle_count == 0 and temp_nodes:
            # Try to schedule remaining nodes in next cycles
            for node, level in temp_nodes:
                queue.append((node, level))
    
    if processed != n:
        print("NO")
        return
        
    # Check if any cycle exceeds T
    for i in range(1, n + 1):
        if cycle[i] > T:
            print("NO")
            return
            
    print("YES")
    print(*cycle[1:])

solve()