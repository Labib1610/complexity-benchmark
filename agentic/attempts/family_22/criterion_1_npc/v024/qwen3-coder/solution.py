from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    M = int(data[1])
    T = int(data[2])
    m = int(data[3])
    
    dependencies = []
    index = 4
    for _ in range(m):
        a = int(data[index])
        b = int(data[index+1])
        dependencies.append((a, b))
        index += 2
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for a, b in dependencies:
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with level tracking
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append((i, 1))  # (reaction, cycle)
    
    result = [0] * (n + 1)
    cycle_count = [0] * (T + 2)  # count of reactions in each cycle
    
    while queue:
        current, cycle = queue.popleft()
        
        # Try to place this reaction in the current cycle
        # If current cycle is full, try the next one
        placement_cycle = cycle
        while placement_cycle <= T and cycle_count[placement_cycle] >= M:
            placement_cycle += 1
            
        if placement_cycle > T:
            print("NO")
            return
            
        result[current] = placement_cycle
        cycle_count[placement_cycle] += 1
        
        # Process neighbors
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                # Neighbor must be placed in a cycle after current's cycle
                queue.append((neighbor, placement_cycle + 1))
    
    # Check if all reactions were scheduled
    for i in range(1, n + 1):
        if result[i] == 0:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, result[1:])))

solve()