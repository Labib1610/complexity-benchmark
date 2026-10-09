from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph and in-degree count
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    # Kahn's algorithm with level tracking (week assignment)
    queue = deque()  # (node, week)
    
    # Find all nodes with in-degree 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append((i, 1))
    
    result = [0] * (n + 1)  # result[i] = week of unit i
    week_counts = [0] * (T + 1)  # week_counts[w] = number of units scheduled in week w
    
    processed = 0
    
    while queue:
        next_queue = deque()
        
        # Group nodes by current week
        current_week_nodes = []
        while queue:
            node, week = queue.popleft()
            current_week_nodes.append((node, week))
        
        # Try to schedule these nodes respecting the M limit per week
        # We process them in the current week if possible, otherwise push to next week
        week_groups = defaultdict(list)  # group nodes by their originally proposed week
        
        for node, week in current_week_nodes:
            week_groups[week].append(node)
            
        for week in sorted(week_groups.keys()):
            nodes = week_groups[week]
            # Try to fit these nodes in their proposed week
            current_count = week_counts[week]
            available_slots = M - current_count
            
            if available_slots >= len(nodes):
                # All can be scheduled in this week
                for node in nodes:
                    result[node] = week
                    week_counts[week] += 1
                    processed += 1
                    
                    # Add neighbors to next week
                    for neighbor in graph[node]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            next_queue.append((neighbor, week + 1))
            else:
                # Some go this week, rest go to next week
                can_schedule = nodes[:available_slots]
                must_delay = nodes[available_slots:]
                
                for node in can_schedule:
                    result[node] = week
                    week_counts[week] += 1
                    processed += 1
                    
                    for neighbor in graph[node]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            next_queue.append((neighbor, week + 1))
                            
                for node in must_delay:
                    result[node] = week
                    week_counts[week] += 1
                    processed += 1
                    
                    for neighbor in graph[node]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            next_queue.append((neighbor, week + 1))
                    
        queue = next_queue
    
    if processed != n:
        print("NO")
        return
        
    # Check if any week exceeds T
    for i in range(1, n + 1):
        if result[i] > T:
            print("NO")
            return
            
    print("YES")
    print(*result[1:])

solve()