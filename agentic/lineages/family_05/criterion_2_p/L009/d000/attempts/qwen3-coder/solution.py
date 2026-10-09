from collections import defaultdict, deque

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
        
    configs = []
    endpoint_to_configs = defaultdict(list)
    shard_to_configs = defaultdict(list)
    ip_to_configs = defaultdict(list)
    
    # Read configurations and build mappings
    for _ in range(t):
        e, d, i = map(int, input().split())
        config = (e, d, i)
        configs.append(config)
        endpoint_to_configs[e].append(len(configs) - 1)
        shard_to_configs[d].append(len(configs) - 1)
        ip_to_configs[i].append(len(configs) - 1)
    
    # Build bipartite graph for matching
    # Nodes: 0..k-1 (endpoints), k..2k-1 (ips)
    # Edges: endpoint e connects to ip i if there exists a config (e, d, i)
    
    adj = defaultdict(list)
    for idx, (e, d, i) in enumerate(configs):
        adj[e-1].append((k+i-1, idx))  # endpoint nodes: 0..k-1, ip nodes: k..2k-1
        adj[k+i-1].append((e-1, idx))
    
    # Hopcroft-Karp algorithm for maximum bipartite matching
    pair_u = [-1] * (2 * k)  # -1 means unmatched
    pair_v = [-1] * (2 * k)
    dist = [0] * (2 * k)
    
    def bfs():
        queue = deque()
        for u in range(k):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[-1] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[-1]:
                for v, _ in adj[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[-1] != float('inf')
    
    def dfs(u):
        if u != -1:
            for v, idx in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(k):
            if pair_u[u] == -1:
                if dfs(u):
                    matching += 1
    
    if matching < k:
        print("NO")
        return
    
    # Reconstruct the solution
    print("YES")
    used_ips = set()
    used_endpoints = set()
    
    # First pass: collect matched pairs
    selected_configs = []
    for u in range(k):
        if pair_u[u] != -1:
            v = pair_u[u]  # v is in range [k, 2k-1], representing IP (v-k+1)
            ip = v - k + 1
            endpoint = u + 1
            
            # Find the actual config that connects this endpoint to this IP
            for idx in endpoint_to_configs[endpoint]:
                e, d, i = configs[idx]
                if e == endpoint and i == ip:
                    selected_configs.append((e, d, i))
                    break
    
    for config in selected_configs:
        print(config[0], config[1], config[2])

solve()