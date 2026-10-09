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
    
    # Kahn's algorithm with phase tracking
    # We'll track for each node, the earliest phase it can start
    phase = [0] * (n + 1)
    queue = deque()
    
    # Find all nodes with in-degree 0
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            phase[i] = 1  # Start in phase 1
    
    processed = 0
    
    # For each phase, we need to respect the bay limit M
    # We'll process nodes level by level according to topological order
    # But we need to make sure that in each phase, we don't exceed M nodes
    
    # Let's reorganize: group nodes by their earliest possible phase
    # Then check if we can fit them within the bay constraints
    
    # First, do a topological sort to get the earliest possible phase for each node
    topo_order = []
    temp_queue = deque(queue)
    temp_in_degree = in_degree[:]
    
    while temp_queue:
        u = temp_queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            temp_in_degree[v] -= 1
            if temp_in_degree[v] == 0:
                temp_queue.append(v)
    
    # Now assign phases respecting both dependencies and bay limits
    # Reset phase array
    phase = [0] * (n + 1)
    assigned = [False] * (n + 1)
    
    # Count of nodes assigned to each phase
    count_in_phase = [0] * (T + 1)
    
    # Queue for nodes ready to be scheduled (in-degree = 0 and not yet assigned)
    ready = deque([i for i in range(1, n+1) if in_degree[i] == 0])
    
    while ready:
        # Group nodes by their earliest possible phase
        # But we need to be more careful - let's simulate phase by phase
        
        # Actually, let's use a different approach:
        # At each step, take nodes with in_degree=0 and try to assign them to the earliest valid phase
        # A node can be assigned to phase p if:
        # 1. All its predecessors are in phases < p
        # 2. count_in_phase[p] < M
        # 3. p <= T
        
        # To make this efficient, for each node, we track the max phase of its predecessors
        # This gives us the earliest phase the node can start
        
        # Let's compute for each node, the maximum phase of its predecessors
        max_pred_phase = [0] * (n + 1)
        
        # When we assign a node to a phase, we update its successors
        # We'll do a greedy assignment
        
        # Sort ready nodes to have deterministic behavior
        current_ready = list(ready)
        ready.clear()
        
        # For each ready node, find the earliest phase it can go to
        for node in current_ready:
            # Earliest phase is max_pred_phase[node] + 1
            earliest = max_pred_phase[node] + 1
            placed = False
            
            for p in range(earliest, T + 1):
                if count_in_phase[p] < M:
                    phase[node] = p
                    assigned[node] = True
                    count_in_phase[p] += 1
                    placed = True
                    
                    # Update successors
                    for succ in graph[node]:
                        in_degree[succ] -= 1
                        max_pred_phase[succ] = max(max_pred_phase[succ], p)
                        if in_degree[succ] == 0:
                            ready.append(succ)
                    break
            
            if not placed:
                print("NO")
                return
    
    # Check if all nodes were assigned
    for i in range(1, n + 1):
        if not assigned[i]:
            print("NO")
            return
    
    print("YES")
    print(*phase[1:])

if __name__ == "__main__":
    main()