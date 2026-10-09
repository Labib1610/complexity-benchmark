import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    idx = 3
    is_spore = [False] * (n + 1)
    for _ in range(t):
        is_spore[int(input_data[idx])] = True
        idx += 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    parent = [0] * (n + 1)
    weight_from_parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    depth[1] = 0
    
    head = 0
    while head < len(order):
        u = order[head]
        head += 1
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                weight_from_parent[v] = w
                depth[v] = depth[u] + 1
                order.append(v)
                
    max_depth = 0
    for i in range(1, n + 1):
        if depth[i] > max_depth:
            max_depth = depth[i]
            
    LOG = max_depth.bit_length()
    up = [[0] * (n + 1) for _ in range(LOG)]
    max_edge = [[0] * (n + 1) for _ in range(LOG)]
    
    for v in range(1, n + 1):
        up[0][v] = parent[v]
        max_edge[0][v] = weight_from_parent[v]
        
    for k in range(1, LOG):
        for v in range(1, n + 1):
            anc = up[k-1][v]
            if anc != 0:
                up[k][v] = up[k-1][anc]
                max_edge[k][v] = max(max_edge[k-1][v], max_edge[k-1][anc])
            else:
                up[k][v] = 0
                max_edge[k][v] = max_edge[k-1][v]
                
    def get_max_edge(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
            
        max_w = 0
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                max_w = max(max_w, max_edge[k][u])
                u = up[k][u]
                
        if u == v:
            return max_w
            
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                max_w = max(max_w, max_edge[k][u], max_edge[k][v])
                u = up[k][u]
                v = up[k][v]
                
        max_w = max(max_w, max_edge[0][u], max_edge[0][v])
        return max_w

    total_cost = 0
    for i in range(n - 1, 0, -1):
        v = order[i]
        p = parent[v]
        if is_spore[v] and not is_spore[p]:
            is_spore[p] = True
            total_cost += weight_from_parent[v]
        elif is_spore[p] and not is_spore[v]:
            total_cost += weight_from_parent[v]
            
    print(total_cost)

if __name__ == '__main__':
    solve()