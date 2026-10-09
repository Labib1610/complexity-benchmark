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
    
    # Topological sort with Kahn's algorithm
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all nodes were visited (no cycles)
    if len(topo_order) != n:
        print("NO")
        return
    
    # Assign phases
    phase = [0] * (n + 1)
    current_phase = 1
    index = 0
    
    while index < n:
        # In each phase, we can assign at most M verses
        assigned_in_phase = 0
        start_index = index
        
        # Try to assign up to M verses that are ready (in-degree is 0)
        temp_queue = []
        for i in range(index, n):
            v = topo_order[i]
            if in_degree[v] <= 0:  # Actually, in_degree is already 0 for these
                temp_queue.append(v)
        
        # Assign the first min(M, len(temp_queue)) verses to this phase
        count = min(M, len(temp_queue))
        for i in range(count):
            v = temp_queue[i]
            phase[v] = current_phase
            # Reduce in-degree of neighbors
            for neighbor in graph[v]:
                in_degree[neighbor] -= 1
        # Update index
        index += count
        
        current_phase += 1
        if current_phase > T:
            print("NO")
            return
            
    # Check if we used more than T phases
    max_phase = max(phase[1:])
    if max_phase > T:
        print("NO")
        return
        
    print("YES")
    print(*phase[1:])

# Run the solution
solve()