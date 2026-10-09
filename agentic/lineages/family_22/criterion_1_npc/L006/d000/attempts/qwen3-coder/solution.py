from collections import defaultdict, deque

def main():
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
    
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we didn't visit all nodes, there's a cycle
    if len(topo_order) != n:
        print("NO")
        return
    
    # Assign cycles using greedy approach
    # For each node, we track the earliest cycle it can start
    min_cycle = [1] * (n + 1)
    
    # Process nodes in topological order
    for node in topo_order:
        for neighbor in graph[node]:
            # Node's neighbors must have cycle > node's cycle
            min_cycle[neighbor] = max(min_cycle[neighbor], min_cycle[node] + 1)
    
    # Check if all cycles are within bounds
    if any(min_cycle[i] > T for i in range(1, n + 1)):
        print("NO")
        return
    
    # Now we need to check if we can fit everything within M steps per cycle
    # Count how many steps are scheduled for each cycle
    cycle_count = [0] * (T + 1)
    result = [0] * (n + 1)
    
    # We'll reassign cycles respecting the M limit
    # Use a greedy approach: for each node in topological order,
    # assign it to the earliest cycle >= min_cycle[node] that has space
    
    for node in topo_order:
        assigned = False
        for cycle in range(min_cycle[node], T + 1):
            if cycle_count[cycle] < M:
                result[node] = cycle
                cycle_count[cycle] += 1
                assigned = True
                break
        if not assigned:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, result[1:])))

if __name__ == "__main__":
    main()