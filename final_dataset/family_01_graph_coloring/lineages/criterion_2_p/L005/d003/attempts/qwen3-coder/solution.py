import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, all machines can be set to mode 1
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # For each connected component, we need to check if a valid assignment exists
    # and find the lexicographically smallest one
    
    assignment = [0] * (n + 1)  # 0 means unassigned
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start] or degree[start] == 0:
            continue
            
        # BFS to get connected component
        component = []
        queue = deque([start])
        visited[start] = True
        component.append(start)
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    component.append(neighbor)
        
        # For each component, try assigning mode 1 to the first unassigned node
        # and propagate constraints
        changed = True
        while changed:
            changed = False
            # Check if current assignments are consistent
            for node in component:
                if assignment[node] != 0:
                    continue
                    
                # Count assigned neighbors
                assigned_neighbors = 0
                unassigned_neighbors = 0
                sum_assigned = 0
                
                for neighbor in adj[node]:
                    if assignment[neighbor] != 0:
                        assigned_neighbors += 1
                        sum_assigned += assignment[neighbor]
                    else:
                        unassigned_neighbors += 1
                
                # If all neighbors are assigned, we can determine node's value
                if assigned_neighbors == degree[node]:
                    if sum_assigned == 2 * degree[node]:
                        assignment[node] = 1
                        changed = True
                    elif sum_assigned == degree[node]:
                        assignment[node] = 2
                        changed = True
                    else:
                        print("NO")
                        return
        
        # Now do a systematic search
        # Try all possible assignments using BFS/DFS would be too slow
        # Let's model this as a 2-SAT problem or use a different approach
        
        # Actually, let's think of the constraint differently:
        # For node u with neighbors N(u), if u=1 then sum of neighbors = 2*|N(u)|
        # If u=2 then sum of neighbors = |N(u)|
        
        # This suggests a more complex relationship. Let's try a greedy approach:
        # Assign nodes in order, and for each node, try mode 1 first (for lex min)
        
        # Reset for this component
        for node in component:
            assignment[node] = 0
            
        # Sort component for deterministic processing
        component.sort()
        
        # Try to assign values
        queue = deque(component)
        attempt_limit = len(component) * 3  # Prevent infinite loops
        attempts = 0
        
        while queue and attempts < attempt_limit:
            attempts += 1
            node = queue.popleft()
            
            if assignment[node] != 0:
                continue
                
            # Check what values are possible for this node
            can_be_1 = True
            can_be_2 = True
            sum_if_1 = 0
            sum_if_2 = 0
            unknown_count = 0
            
            for neighbor in adj[node]:
                if assignment[neighbor] != 0:
                    sum_if_1 += assignment[neighbor]
                    sum_if_2 += assignment[neighbor]
                else:
                    unknown_count += 1
            
            # If all neighbors are assigned, check constraints
            if unknown_count == 0:
                # Node can be 1 if sum of neighbors = 2 * degree[node]
                if sum_if_1 != 2 * degree[node]:
                    can_be_1 = False
                # Node can be 2 if sum of neighbors = degree[node]
                if sum_if_1 != degree[node]:
                    can_be_2 = False
                
                if not can_be_1 and not can_be_2:
                    print("NO")
                    return
                elif can_be_1:  # Prefer mode 1 for lexicographically smallest
                    assignment[node] = 1
                elif can_be_2:
                    assignment[node] = 2
            else:
                # Not all neighbors assigned, put back in queue
                queue.append(node)
                continue
        
        # If there are still unassigned nodes, the problem might be unsolvable
        # or we need a more sophisticated approach
        
        # Let's do a final check
        unassigned_exists = False
        for node in component:
            if assignment[node] == 0:
                unassigned_exists = True
                break
                
        if unassigned_exists:
            # Try a different approach - fix one node and propagate
            # Find node with highest degree to start
            max_degree = -1
            start_node = component[0]
            for node in component:
                if degree[node] > max_degree:
                    max_degree = degree[node]
                    start_node = node
            
            # Reset assignments for this component
            for node in component:
                assignment[node] = 0
                
            # Try mode 1 for start_node
            assignment[start_node] = 1
            to_process = deque([start_node])
            processed = set()
            
            while to_process:
                current = to_process.popleft()
                if current in processed:
                    continue
                processed.add(current)
                
                # For each neighbor of current, check if we can determine its value
                for neighbor in adj[current]:
                    if assignment[neighbor] != 0:
                        continue
                        
                    # Count how many of neighbor's neighbors are assigned
                    assigned_nbrs_sum = 0
                    assigned_nbrs_count = 0
                    for nn in adj[neighbor]:
                        if assignment[nn] != 0:
                            assigned_nbrs_sum += assignment[nn]
                            assigned_nbrs_count += 1
                    
                    # If all neighbors of neighbor are assigned, determine its value
                    if assigned_nbrs_count == degree[neighbor]:
                        # Check both possibilities
                        if assigned_nbrs_sum == 2 * degree[neighbor]:  # neighbor should be 1
                            assignment[neighbor] = 1
                            to_process.append(neighbor)
                        elif assigned_nbrs_sum == degree[neighbor]:   # neighbor should be 2
                            assignment[neighbor] = 2
                            to_process.append(neighbor)
                        else:
                            print("NO")
                            return
            
            # Check if all nodes in component are assigned
            for node in component:
                if assignment[node] == 0:
                    # Try mode 2 for start_node instead
                    for n_node in component:
                        assignment[n_node] = 0
                        
                    assignment[start_node] = 2
                    to_process = deque([start_node])
                    processed = set()
                    
                    while to_process:
                        current = to_process.popleft()
                        if current in processed:
                            continue
                        processed.add(current)
                        
                        for neighbor in adj[current]:
                            if assignment[neighbor] != 0:
                                continue
                                
                            assigned_nbrs_sum = 0
                            assigned_nbrs_count = 0
                            for nn in adj[neighbor]:
                                if assignment[nn] != 0:
                                    assigned_nbrs_sum += assignment[nn]
                                    assigned_nbrs_count += 1
                            
                            if assigned_nbrs_count == degree[neighbor]:
                                if assigned_nbrs_sum == 2 * degree[neighbor]:
                                    assignment[neighbor] = 1
                                    to_process.append(neighbor)
                                elif assigned_nbrs_sum == degree[neighbor]:
                                    assignment[neighbor] = 2
                                    to_process.append(neighbor)
                                else:
                                    print("NO")
                                    return
                    break
                    
            # Final check
            for node in component:
                if assignment[node] == 0:
                    print("NO")
                    return
    
    # Verify solution
    for u in range(1, n + 1):
        if degree[u] == 0:
            assignment[u] = 1  # Default for isolated nodes
            continue
        if assignment[u] == 0:
            assignment[u] = 1  # Default
            
        neighbor_sum = sum(assignment[v] for v in adj[u])
        if assignment[u] == 1 and neighbor_sum != 2 * degree[u]:
            print("NO")
            return
        if assignment[u] == 2 and neighbor_sum != degree[u]:
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))

solve()