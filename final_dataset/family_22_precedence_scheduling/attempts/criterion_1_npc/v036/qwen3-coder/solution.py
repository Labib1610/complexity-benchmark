from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with level assignment
    queue = deque()
    level = [0] * (n + 1)
    
    # Find all nodes with indegree 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            level[i] = 1
    
    processed = 0
    while queue:
        current = queue.popleft()
        processed += 1
        
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            # Update level: neighbor must be processed after current
            level[neighbor] = max(level[neighbor], level[current] + 1)
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all compounds were processed (no cycles)
    if processed != n:
        print("NO")
        return
    
    # Check if we need more than T stages
    max_level = max(level[1:])
    if max_level > T:
        print("NO")
        return
    
    # Group compounds by level
    compounds_by_level = defaultdict(list)
    for i in range(1, n + 1):
        compounds_by_level[level[i]].append(i)
    
    # Check if any level exceeds M compounds
    for lvl in range(1, max_level + 1):
        if len(compounds_by_level[lvl]) > M:
            print("NO")
            return
    
    # Output result
    print("YES")
    print(*level[1:])

solve()