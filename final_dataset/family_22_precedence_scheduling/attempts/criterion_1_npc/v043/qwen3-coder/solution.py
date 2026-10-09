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
    
    # Topological sort with level constraint
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = [0] * (n + 1)
    shift = 1
    placed_count = 0
    
    while shift <= T and placed_count < n:
        # Get all nodes with in-degree 0 for this shift
        current_shift_nodes = []
        cranes_used = 0
        
        # We can place at most M nodes in each shift
        while queue and cranes_used < M:
            node = queue.popleft()
            result[node] = shift
            current_shift_nodes.append(node)
            cranes_used += 1
            placed_count += 1
        
        # If no nodes can be placed in this shift but we haven't finished, it's impossible
        if cranes_used == 0 and placed_count < n:
            print("NO")
            return
        
        # Update in-degrees for next level
        for node in current_shift_nodes:
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        shift += 1
    
    # Check if all nodes were placed
    if placed_count < n:
        print("NO")
        return
    
    print("YES")
    print(*result[1:])

solve()