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
    
    # Topological sort with cycle detection
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we didn't visit all nodes, there's a cycle
    if len(topological_order) != n:
        print("NO")
        return
    
    # Assign operations to cycles
    assignment = [0] * (n + 1)
    cycle_operations = [[] for _ in range(T + 1)]
    
    # For each operation in topological order
    for op in topological_order:
        # Find the earliest cycle where all prerequisites are done
        earliest_cycle = 1
        for prereq in graph:
            if op in graph[prereq]:
                earliest_cycle = max(earliest_cycle, assignment[prereq] + 1)
        
        # Find the first available cycle with space
        assigned = False
        for cycle in range(earliest_cycle, T + 1):
            if len(cycle_operations[cycle]) < M:
                cycle_operations[cycle].append(op)
                assignment[op] = cycle
                assigned = True
                break
        
        if not assigned:
            print("NO")
            return
    
    print("YES")
    print(*[assignment[i] for i in range(1, n + 1)])

solve()