from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    records = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        records.append((a, b, c))
    
    # If q is 0, we need 0 records
    if q == 0:
        print("YES")
        return
    
    # If we have no records but need some, impossible
    if t == 0:
        print("NO")
        return
    
    # Build graph for matching
    # Each person is a node on the left, each record is a node on the right
    # We want a matching that covers all 3*q people
    
    # This is a 3D matching problem, but we can reduce it to max flow
    # Create a flow network:
    # Source -> each record (capacity 1)
    # Each record -> its 3 people (capacity 1 each)
    # Each person -> sink (capacity 1)
    
    # But actually, since each record must be used at most once, and each person at most once,
    # this is a matching problem in a 3-uniform hypergraph, which we can solve with max flow
    
    # Let's model this as a flow network
    # Nodes: 0 (source), 1..t (records), t+1..t+3*q (people), t+3*q+1 (sink)
    # Edges: source to each record (capacity 1)
    #        each record to its 3 people (capacity 1)
    #        each person to sink (capacity 1)
    
    # But max flow might be overkill. Let's try a greedy approach first.
    # Actually, let's use max flow since this is the correct approach.
    
    # Use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    SOURCE = 0
    SINK = t + 3*q + 1
    # Records are 1..t
    # People are t+1..t+3*q
    
    # Build adjacency list and capacity matrix
    adj = defaultdict(list)
    capacity = defaultdict(int)
    
    # Source to records
    for i in range(1, t+1):
        adj[SOURCE].append(i)
        adj[i].append(SOURCE)
        capacity[(SOURCE, i)] = 1
    
    # Records to people
    for i in range(t):
        a, b, c = records[i]
        record_node = i + 1
        person_a = t + a
        person_b = t + b
        person_c = t + c
        
        adj[record_node].extend([person_a, person_b, person_c])
        adj[person_a].append(record_node)
        adj[person_b].append(record_node)
        adj[person_c].append(record_node)
        
        capacity[(record_node, person_a)] = 1
        capacity[(record_node, person_b)] = 1
        capacity[(record_node, person_c)] = 1
    
    # People to sink
    for i in range(1, 3*q + 1):
        person_node = t + i
        adj[person_node].append(SINK)
        adj[SINK].append(person_node)
        capacity[(person_node, SINK)] = 1
    
    # Max flow implementation
    def bfs():
        # Returns a path from source to sink if exists, otherwise None
        parent = [-1] * (t + 3*q + 2)
        visited = [False] * (t + 3*q + 2)
        queue = deque([SOURCE])
        visited[SOURCE] = True
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if not visited[v] and capacity[(u, v)] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == SINK:
                        # Reconstruct path
                        path = []
                        cur = SINK
                        while cur != -1:
                            path.append(cur)
                            cur = parent[cur]
                        return path[::-1]
        
        return None
    
    # Edmonds-Karp
    max_flow = 0
    while True:
        path = bfs()
        if not path:
            break
            
        # Find minimum capacity along the path
        min_cap = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            min_cap = min(min_cap, capacity[(u, v)])
        
        # Update capacities
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            capacity[(u, v)] -= min_cap
            capacity[(v, u)] += min_cap
        
        max_flow += min_cap
    
    if max_flow != 3*q:  # We need to match all 3*q people, but flow is number of records used
        # Wait, max_flow is the number of people matched, which should be 3*q for full staffing
        # But in our model, max_flow is also the number of records used, which should be q
        # There's a mismatch. Let me recheck.
        # Actually, max_flow should equal both: number of records used = q, number of people matched = 3*q
        # But in flow, value = q (records) = 3*q (people) / 3. This is inconsistent.
        # Let me think differently.
        pass
    
    # Let me reconsider the flow value.
    # Each unit of flow corresponds to one record being used, which covers 3 people.
    # So max_flow units of flow cover 3*max_flow people.
    # We want 3*max_flow = 3*q, so max_flow = q.
    
    if max_flow != q:
        print("NO")
        return
    
    # Reconstruct the solution
    print("YES")
    
    # Find which records are used
    selected_records = []
    for i in range(1, t+1):
        # If there's flow from source to record i, it's selected
        if capacity[(SOURCE, i)] == 0:  # Original capacity was 1, now 0
            selected_records.append(i-1)  # Convert to 0-based index
    
    # Output the selected records
    for idx in selected_records:
        a, b, c = records[idx]
        print(a, b, c)

solve()