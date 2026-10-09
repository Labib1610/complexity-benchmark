import sys
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(iterator))
        l2 = int(next(iterator))
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        s1 = 1 if l1 > 0 else 0
        s2 = 1 if l2 > 0 else 0
        
        # Clause: (u in state s1) OR (v in state s2)
        # Implications:
        # not(u is s1) -> (v is s2)
        # not(v is s2) -> (u is s1)
        
        # Node indices: 2*i for False(0), 2*i+1 for True(1)
        nu = 2 * u + (1 - s1) # not(u is s1)
        tv = 2 * v + s2       # v is s2
        adj[nu].append(tv)
        
        nv = 2 * v + (1 - s2) # not(v is s2)
        tu = 2 * u + s1       # u is s1
        adj[nv].append(tu)
        
    # Kosaraju's algorithm for Strongly Connected Components
    num_nodes = 2 * n
    visited = [False] * num_nodes
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                neighbor = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[neighbor]:
                    stack.append((neighbor, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(num_nodes):
        if not visited[i]:
            dfs1(i)
            
    adj_rev = [[] for _ in range(num_nodes)]
    for u in range(num_nodes):
        for v in adj[u]:
            adj_rev[v].append(u)
            
    visited = [False] * num_nodes
    comp_id = [-1] * num_nodes
    current_id = 0
    
    def dfs2(u, current_id):
        stack = [u]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            comp_id[node] = current_id
            for neighbor in adj_rev[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    for u in reversed(order):
        if not visited[u]:
            dfs2(u, current_id)
            current_id += 1
            
    assignment = [0] * n
    for i in range(n):
        node_true = 2 * i + 1
        node_false = 2 * i
        if comp_id[node_true] == comp_id[node_false]:
            sys.stdout.write("NO\n")
            return
        assignment[i] = 1 if comp_id[node_true] > comp_id[node_false] else 0
        
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, assignment)) + "\n")

solve()