import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n + 2)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # l1 is a literal: positive means var is true, negative means var is false
        # We need (l1 OR l2)
        # Implication: not l1 -> l2 and not l2 -> l1
        
        # Convert literal to node index
        # Node indices: 1 to n for positive literals, n+1 to 2n for negative literals
        # Literal x: if x > 0, node = x; if x < 0, node = n + |x|
        
        def get_node(lit):
            if lit > 0:
                return lit
            else:
                return n + (-lit)
        
        u = get_node(l1)
        v = get_node(l2)
        
        # not u -> v
        not_u = u + n if u <= n else u - n
        adj[not_u].append(v)
        
        # not v -> u
        not_v = v + n if v <= n else v - n
        adj[not_v].append(u)
    
    # Kosaraju's algorithm to find SCCs
    visited = [False] * (2 * n + 1)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for i in range(len(adj[node]) - 1, -1, -1):
                    v = adj[node][i]
                    if not visited[v]:
                        stack.append((v, 0))
            else:
                order.append(node)
    
    for i in range(1, 2 * n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Build reverse graph
    radj = [[] for _ in range(2 * n + 1)]
    for u in range(1, 2 * n + 1):
        for v in adj[u]:
            radj[v].append(u)
    
    comp = [-1] * (2 * n + 1)
    current_comp = 0
    
    def dfs2(u, label):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = label
            for v in radj[node]:
                if comp[v] == -1:
                    stack.append(v)
    
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1
    
    # Check for contradiction
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if comp[i] == comp[i + n]:
            print("NO")
            return
        assignment[i] = 1 if comp[i] > comp[i + n] else 0
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

solve()