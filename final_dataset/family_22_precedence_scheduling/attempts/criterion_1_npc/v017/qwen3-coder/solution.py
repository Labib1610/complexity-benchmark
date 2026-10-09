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
    
    # Topological sort with level assignment
    queue = deque()
    # Find all nodes with in-degree 0
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # Assignment of operations to cycles
    assignment = [0] * (n + 1)
    current_cycle = 1
    operations_in_current_cycle = 0
    completed = 0
    
    while queue and current_cycle <= T:
        next_queue = deque()
        operations_in_current_cycle = 0
        
        # Process up to M operations in current cycle
        while queue and operations_in_current_cycle < M:
            node = queue.popleft()
            assignment[node] = current_cycle
            operations_in_current_cycle += 1
            completed += 1
            
            # Update neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_queue.append(neighbor)
        
        # Move to next cycle
        current_cycle += 1
        queue = next_queue
    
    # If there are still unprocessed nodes, it means we either ran out of time or have a cycle
    if completed < n:
        print("NO")
        return
    
    print("YES")
    print(*assignment[1:])

solve()