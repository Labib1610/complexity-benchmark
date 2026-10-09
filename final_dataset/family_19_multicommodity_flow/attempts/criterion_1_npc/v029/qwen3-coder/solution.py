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
    
    # item types: (source, target, demand)
    items = []
    for i in range(k):
        s = int(data[idx]) - 1  # convert to 0-based
        idx += 1
        t = int(data[idx]) - 1
        idx += 1
        d = int(data[idx])
        idx += 1
        items.append((s, t, d))
    
    # links: (u, v, limit)
    links = []
    link_map = {}  # (u,v) -> index
    for i in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        limit = int(data[idx])
        idx += 1
        links.append((u, v, limit))
        link_map[(u, v)] = i
    
    # Build graph for flow
    # For each item type, we need to find a flow from s to t with value d
    # But all flows share the same edges with capacities
    
    # We will use a multi-commodity flow approach with integer flows
    # This is NP-hard in general, but since the constraints are small, we can try a method:
    # Try to find integer flows for each commodity one by one, respecting the global capacity constraints
    
    # Initialize usage of each link to 0
    usage = [0] * m
    # For each item type, store the flow on each link
    flows = [ [0] * m for _ in range(k) ]
    
    # Build adjacency list for the graph
    adj = defaultdict(list)
    for u, v, _ in links:
        adj[u].append(v)
        adj[v].append(u)  # for reverse traversal in BFS
    
    # Function to find a path from s to t in the graph
    def bfs_path(s, t):
        visited = [False] * n
        parent = [-1] * n
        queue = deque()
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            if u == t:
                break
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        
        if not visited[t]:
            return None  # No path
        
        # Reconstruct path
        path = []
        cur = t
        while parent[cur] != -1:
            path.append((parent[cur], cur))
            cur = parent[cur]
        path.reverse()
        return path
    
    # Function to find a flow of value 'amount' for item (s,t,amount)
    # respecting current usage and link limits
    def find_flow(s, t, amount):
        # We need to find 'amount' edge-disjoint paths or a way to send 'amount' flow
        # Since we are dealing with integer flows and small numbers, we can try to send one unit at a time
        local_flow = [0] * m
        current_amount = 0
        
        while current_amount < amount:
            # Find a path from s to t
            path = bfs_path(s, t)
            if path is None:
                return None  # Cannot send more flow
            
            # Find the minimum residual capacity along the path
            min_res = float('inf')
            for u, v in path:
                link_idx = link_map.get((u, v), -1)
                if link_idx == -1:
                    # This should not happen
                    return None
                res_cap = links[link_idx][2] - usage[link_idx] - local_flow[link_idx]
                if res_cap < min_res:
                    min_res = res_cap
            
            if min_res <= 0:
                return None  # No residual capacity
            
            # Send at least 1 unit
            send = min(min_res, amount - current_amount)
            if send <= 0:
                return None
            
            # Update local flow
            for u, v in path:
                link_idx = link_map[(u, v)]
                local_flow[link_idx] += send
            
            current_amount += send
        
        return local_flow
    
    # Try to assign flows for each item
    for i in range(k):
        s, t, d = items[i]
        flow = find_flow(s, t, d)
        if flow is None:
            print("NO")
            return
        # Update global usage
        for j in range(m):
            usage[j] += flow[j]
        flows[i] = flow
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, flows[i])))

solve()