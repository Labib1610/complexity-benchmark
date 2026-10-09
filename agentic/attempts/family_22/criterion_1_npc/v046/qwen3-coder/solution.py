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
    
    # Find all nodes with in-degree 0
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # Term assignment for each module (1-indexed)
    term_assignment = [0] * (n + 1)
    
    # Process each term
    current_term = 1
    modules_processed = 0
    
    while current_term <= T and queue:
        # Limit modules in current term by capacity M
        modules_this_term = 0
        next_queue = deque()
        
        # Process modules for current term
        while queue and modules_this_term < M:
            node = queue.popleft()
            term_assignment[node] = current_term
            modules_processed += 1
            modules_this_term += 1
            
            # Update neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_queue.append(neighbor)
        
        # Carry over unprocessed nodes to next term
        while queue:
            next_queue.append(queue.popleft())
            
        queue = next_queue
        current_term += 1
    
    # Check if all modules were processed
    if modules_processed != n:
        print("NO")
        return
    
    print("YES")
    print(*term_assignment[1:])

solve()