from collections import defaultdict, deque
import sys

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    swarms = []
    for _ in range(k):
        s = int(data[idx])
        idx += 1
        t = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        swarms.append((s, t, d))
        
    corridors = []
    cap = []
    graph = defaultdict(list)
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        c = int(data[idx])
        idx += 1
        corridors.append((u, v))
        cap.append(c)
        graph[u].append((v, i))
    
    # For each swarm, we need to find a flow from source to sink
    # We'll model this as a multi-commodity flow problem
    # But since each swarm is indivisible, we need to find paths for each drone
    # However, we can think of it as sending 'd' units of flow for each swarm
    
    # Let's build a combined flow network where we track usage per corridor
    # We will use a greedy approach with max-flow for each swarm considering current usage
    
    from collections import deque, defaultdict
    
    def bfs_flow(source, sink, capacity, usage, graph_nodes):
        # BFS to find augmenting path
        parent = {}
        visited = set()
        queue = deque([source])
        visited.add(source)
        parent[source] = None
        
        while queue:
            u = queue.popleft()
            if u == sink:
                break
            for v, edge_id in graph_nodes[u]:
                if v not in visited and usage[edge_id] < capacity[edge_id]:
                    visited.add(v)
                    parent[v] = (u, edge_id)
                    queue.append(v)
                    
        if sink not in parent:
            return None
            
        # Reconstruct path
        path = []
        current = sink
        while parent[current] is not None:
            prev_node, edge_id = parent[current]
            path.append(edge_id)
            current = prev_node
        path.reverse()
        return path
    
    def find_flow_paths(source, sink, demand, capacity, usage, graph_nodes):
        # Try to send 'demand' units of flow from source to sink
        paths_per_unit = []
        temp_usage = usage[:]
        success = True
        
        for _ in range(demand):
            path = bfs_flow(source, sink, capacity, temp_usage, graph_nodes)
            if path is None:
                success = False
                break
            paths_per_unit.append(path)
            for e in path:
                temp_usage[e] += 1
                
        return success, paths_per_unit, temp_usage
    
    # Initialize usage to zero
    current_usage = [0] * m
    
    # Store paths for each swarm
    swarm_flows = []
    
    # Process each swarm
    for i, (s, t, d) in enumerate(swarms):
        # Try to find paths for this swarm given current usage
        success, paths, new_usage = find_flow_paths(s, t, d, cap, current_usage, graph)
        if not success:
            print("NO")
            return
            
        # Update usage
        current_usage = new_usage
        swarm_flows.append(paths)
    
    # If we get here, we have a solution
    print("YES")
    
    # Now we need to convert paths to edge counts per swarm
    result = []
    for i, paths_list in enumerate(swarm_flows):
        edge_count = [0] * m
        for paths in paths_list:
            for e in paths:
                edge_count[e] += 1
        result.append(edge_count)
    
    for counts in result:
        print(' '.join(map(str, counts)))

solve()