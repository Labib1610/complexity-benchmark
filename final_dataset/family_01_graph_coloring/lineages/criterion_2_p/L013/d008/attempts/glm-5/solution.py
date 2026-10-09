import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr += 1
    m = int(input[ptr]); ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    edges = []
    for _ in range(m):
        u = int(input[ptr]); v = int(input[ptr+1]); ptr += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    # BFS to find components and check bipartiteness
    color = [0] * (n + 1)
    comp_id = [0] * (n + 1)
    comp_cnt = [0, 0]
    comps = []
    
    for i in range(1, n + 1):
        if color[i] == 0:
            comp_cnt = [0, 0]
            q = deque([i])
            color[i] = 1
            comp_cnt[0] = 1
            comp_nodes = []
            
            while q:
                u = q.popleft()
                comp_nodes.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        comp_cnt[color[v] - 1] += 1
                        q.append(v)
            
            comps.append((comp_nodes, comp_cnt[:]))
    
    # Check if any component is non-bipartite
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
    
    # Count edges in each component
    comp_edges = [0] * len(comps)
    comp_of = [0] * (n + 1)
    for idx, (nodes, _) in enumerate(comps):
        for node in nodes:
            comp_of[node] = idx
    
    for u, v in edges:
        comp_edges[comp_of[u]] += 1
    
    # Check if all components have exactly 2m/9 edges
    # For a bipartite graph with a edges, stability sum is 2a/9
    # We need 2m/9, so we need sum of edges = m, which is always true
    # But we need each component to contribute 2*edges/9
    # Total = sum of 2*edges/9 = 2m/9, which is satisfied automatically
    
    # So any bipartite coloring works. We need to maximize confidence score.
    # Confidence = sum of (2-p_i)/i! = sum of 2/i! - sum of p_i/i!
    # To maximize, minimize sum of p_i/i!
    # p_i in {1,2}, so we want p_i=1 when i! is small (i is small)
    
    # For each component, we can flip colors. 
    # Cost of current assignment: sum of p_i/i! for all i
    # If we flip, nodes with color 1 become p=2, color 2 become p=1
    
    # Compute cost for each component in both orientations
    comp_cost = []  # (cost_diff, comp_idx)
    total_cost = 0
    
    for idx, (nodes, cnt) in enumerate(comps):
        cost1 = 0  # cost when color 1 -> p=1, color 2 -> p=2
        cost2 = 0  # cost when color 1 -> p=2, color 2 -> p=1
        for node in nodes:
            fact = 1
            for _ in range(1, node):
                fact *= _
            c = color[node]
            if c == 1:
                cost1 += 1.0 / fact
                cost2 += 2.0 / fact
            else:
                cost1 += 2.0 / fact
                cost2 += 1.0 / fact
        total_cost += min(cost1, cost2)
        comp_cost.append((cost2 - cost1, idx))
    
    # Greedily flip components with negative cost_diff
    comp_cost.sort()
    flip = [False] * len(comps)
    for diff, idx in comp_cost:
        if diff < 0:
            flip[idx] = True
            total_cost += diff
        else:
            break
    
    # Build answer
    ans = [0] * (n + 1)
    for idx, (nodes, _) in enumerate(comps):
        for node in nodes:
            c = color[node]
            if flip[idx]:
                c = 3 - c
            ans[node] = c
    
    print("YES")
    print(' '.join(map(str, ans[1:])))

if __name__ == "__main__":
    solve()