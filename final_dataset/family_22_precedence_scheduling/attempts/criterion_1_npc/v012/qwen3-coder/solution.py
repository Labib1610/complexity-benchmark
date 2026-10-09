from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    # Topological sort with priority queue to get lexicographically smallest order
    from heapq import heappush, heappop
    
    # Find all nodes with in-degree 0
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heappush(heap, i)
    
    # Week assignment
    week = [0] * (n + 1)
    week_count = [0] * (T + 1)  # Number of sectors assigned to each week
    
    # Process nodes in topological order
    while heap:
        # Get the earliest week that has space and satisfies dependencies
        current = heappop(heap)
        
        # Find the earliest week where we can place this sector
        earliest_week = 1
        
        # Check all predecessors to ensure we start after them
        for prev in range(1, n + 1):
            if current in graph[prev]:
                earliest_week = max(earliest_week, week[prev] + 1)
        
        # Find first week from earliest_week onwards that has space
        assigned_week = -1
        for w in range(earliest_week, T + 1):
            if week_count[w] < M:
                assigned_week = w
                break
        
        if assigned_week == -1:
            print("NO")
            return
            
        week[current] = assigned_week
        week_count[assigned_week] += 1
        
        # Reduce in-degree of neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heappush(heap, neighbor)
    
    # Check if all nodes were processed
    for i in range(1, n + 1):
        if week[i] == 0:
            print("NO")
            return
    
    print("YES")
    print(*week[1:])

solve()