from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph for dependencies
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    # Topological sort to get a valid order
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
    
    # If we couldn't process all nodes, there's a cycle
    if len(topo_order) != n:
        print("NO")
        return
    
    # Assign servings
    serving_assignment = [0] * (n + 1)
    current_serving = 1
    index = 0
    
    while index < n:
        # Fill current serving with up to M items
        count_in_current = 0
        temp_index = index
        
        # Check how many we can put in current serving
        while temp_index < n and count_in_current < M:
            item = topo_order[temp_index]
            can_assign = True
            
            # Check if all dependencies are in previous servings
            for dep in graph[item]:
                if serving_assignment[dep] == 0 or serving_assignment[dep] >= current_serving:
                    can_assign = False
                    break
            
            if can_assign or serving_assignment[item] == 0:
                count_in_current += 1
                temp_index += 1
            else:
                break
        
        # Actually assign them
        assigned_count = 0
        i = index
        while i < index + count_in_current and assigned_count < M:
            item = topo_order[i]
            # Double-check dependencies
            can_assign = True
            for dep in graph[item]:
                if serving_assignment[dep] == 0 or serving_assignment[dep] >= current_serving:
                    can_assign = False
                    break
            
            if can_assign and serving_assignment[item] == 0:
                serving_assignment[item] = current_serving
                assigned_count += 1
            i += 1
        
        if assigned_count == 0:
            print("NO")
            return
            
        index += assigned_count
        current_serving += 1
        
        if current_serving > T:
            print("NO")
            return
    
    # Verify all items were assigned
    for i in range(1, n + 1):
        if serving_assignment[i] == 0:
            print("NO")
            return
    
    print("YES")
    print(*serving_assignment[1:])

solve()