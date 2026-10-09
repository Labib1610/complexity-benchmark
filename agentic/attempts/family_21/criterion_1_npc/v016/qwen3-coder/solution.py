import sys
from collections import defaultdict, deque

def find_connected_components(n, edges, sealed):
    adj = defaultdict(list)
    for u, v, _ in edges:
        if (u, v) not in sealed and (v, u) not in sealed:
            adj[u].append(v)
            adj[v].append(u)
    
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            components.append(component)
    
    return components

def check_isolation(containment_sites, components):
    site_to_component = {}
    for i, component in enumerate(components):
        for site in containment_sites:
            if site in component:
                if site in site_to_component:
                    return False
                site_to_component[site] = i
    
    # Check if all containment sites are in different components
    return len(site_to_component) == len(containment_sites) and len(set(site_to_component.values())) == len(containment_sites)

def solve():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    containment_sites = []
    for _ in range(k):
        containment_sites.append(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))
    
    # Try all possible combinations of corridors to seal
    # Since m can be up to 20, we can use bit manipulation
    best_cost = B + 1
    best_sealed = None
    
    for mask in range(1 << m):
        sealed = []
        cost = 0
        sealed_set = set()
        
        for i in range(m):
            if mask & (1 << i):
                u, v, w = edges[i]
                sealed.append((u, v))
                sealed_set.add((u, v))
                cost += w
        
        if cost > B:
            continue
            
        # Check if this sealing satisfies the conditions
        components = find_connected_components(n, edges, sealed_set)
        
        if len(components) < k:
            continue
            
        if check_isolation(containment_sites, components):
            if cost < best_cost:
                best_cost = cost
                best_sealed = sealed[:]
    
    if best_sealed is not None:
        print("YES")
        print(len(best_sealed))
        for u, v in best_sealed:
            print(u, v)
    else:
        print("NO")

solve()