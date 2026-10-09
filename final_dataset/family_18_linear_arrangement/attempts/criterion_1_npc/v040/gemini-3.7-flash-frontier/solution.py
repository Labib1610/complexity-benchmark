import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            q = [i]
            visited[i] = True
            for node in q:
                comp.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)
            components.append(comp)
            
    total_cost = 0
    full_order = []
    
    def solve_component(nodes):
        k = len(nodes)
        if k == 1:
            return 0, nodes
        
        node_to_idx = {node: i for i, node in enumerate(nodes)}
        comp_adj = [0] * k
        comp_deg = [0] * k
        
        for u_node in nodes:
            u_idx = node_to_idx[u_node]
            for v_node in adj[u_node]:
                if v_node in node_to_idx:
                    v_idx = node_to_idx[v_node]
                    comp_adj[u_idx] |= (1 << v_idx)
            comp_deg[u_idx] = comp_adj[u_idx].bit_count()
            
        size = 1 << k
        cut = [0] * size
        for mask in range(1, size):
            lsb = mask & -mask
            u = lsb.bit_length() - 1
            prev = mask ^ lsb
            cut[mask] = cut[prev] + comp_deg[u] - 2 * (prev & comp_adj[u]).bit_count()
            
        dp = [10**9] * size
        parent = [0] * size
        dp[0] = 0
        
        for mask in range(size - 1):
            c_dp = dp[mask]
            rem = (~mask) & (size - 1)
            while rem:
                lsb = rem & -rem
                u = lsb.bit_length() - 1
                nmask = mask | lsb
                ncost = c_dp + cut[nmask]
                if ncost < dp[nmask]:
                    dp[nmask] = ncost
                    parent[nmask] = u
                rem ^= lsb
                
        order = []
        curr = size - 1
        while curr > 0:
            u = parent[curr]
            order.append(nodes[u])
            curr ^= (1 << u)
        order.reverse()
        return dp[size - 1], order

    for comp in components:
        cost, order = solve_component(comp)
        total_cost += cost
        full_order.extend(order)
        
    if total_cost <= B:
        print("YES")
        bays = [0] * (n + 1)
        for bay_idx, asm in enumerate(full_order, start=1):
            bays[asm] = bay_idx
        print(*(bays[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()