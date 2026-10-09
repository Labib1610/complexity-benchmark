from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    configs = []
    endpoint_to_shard = {}
    
    for _ in range(t):
        e = int(data[index])
        d = int(data[index+1])
        i = int(data[index+2])
        configs.append((e, d, i))
        endpoint_to_shard[e] = d
        index += 3
    
    # Since each endpoint maps to exactly one shard and all shards are distinct,
    # we can group configurations by endpoint
    config_dict = defaultdict(list)
    for e, d, i in configs:
        config_dict[e].append((e, d, i))
    
    # Build a bipartite graph between endpoints and IPs
    # Each endpoint can use any of its available IPs
    # We need a perfect matching where each endpoint gets one IP
    
    # Create adjacency list for endpoints to available IPs
    adj = defaultdict(list)
    for e in config_dict:
        for e_val, d_val, i_val in config_dict[e]:
            adj[e].append(i_val)
    
    # Use Hopcroft-Karp or similar for maximum bipartite matching
    # But since k <= 1200, we can use a simpler approach like DFS-based matching
    
    match_ip_to_endpoint = {}  # ip -> endpoint
    match_endpoint_to_ip = {}  # endpoint -> ip
    
    def dfs(ep, visited_ips):
        for ip in adj[ep]:
            if ip in visited_ips:
                continue
            visited_ips.add(ip)
            # If this IP is free or we can rematch its current endpoint
            if ip not in match_ip_to_endpoint:
                match_ip_to_endpoint[ip] = ep
                match_endpoint_to_ip[ep] = ip
                return True
            else:
                old_ep = match_ip_to_endpoint[ip]
                if dfs(old_ep, visited_ips):
                    match_ip_to_endpoint[ip] = ep
                    match_endpoint_to_ip[ep] = ip
                    return True
        return False
    
    # Try to find a matching for all endpoints
    matched = 0
    for e in config_dict:
        visited_ips = set()
        if dfs(e, visited_ips):
            matched += 1
    
    if matched < k:
        print("NO")
        return
    
    print("YES")
    result_configs = []
    for e in range(1, k+1):
        ip = match_endpoint_to_ip[e]
        # Find the original config with this endpoint and IP
        for cfg in config_dict[e]:
            if cfg[2] == ip:
                result_configs.append(cfg)
                break
    
    for c in result_configs:
        print(c[0], c[1], c[2])

solve()