import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph for 2-SAT
    # Variable x_i: True -> ENERGIZED (1), False -> ISOLATED (0)
    # Node indices: 2*i for False, 2*i+1 for True (0-indexed)
    # For each clause (a OR b), add edges: not a -> b, not b -> a
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # Process l1
        if l1 > 0:
            u = l1 - 1  # 0-indexed variable
            # l1 means x_u = True
            # not l1 means x_u = False
            u_true = 2 * u + 1
            u_false = 2 * u
        else:
            u = -l1 - 1
            # l1 = -u-1 means x_u = False
            # not l1 means x_u = True
            u_true = 2 * u
            u_false = 2 * u + 1
        
        # Process l2
        if l2 > 0:
            v = l2 - 1
            v_true = 2 * v + 1
            v_false = 2 * v
        else:
            v = -l2 - 1
            v_true = 2 * v
            v_false = 2 * v + 1
        
        # Add edges: not l1 -> l2, not l2 -> l1
        adj[u_false].append(v_true)
        adj[v_false].append(u_true)
    
    # Kosaraju's algorithm for SCC
    # Pass 1: compute finish order
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                v = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[v]:
                    stack.append((v, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Build reverse graph
    radj = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            radj[v].append(u)
    
    # Pass 2: find SCCs in reverse order
    comp = [-1] * (2 * n)
    comp_id = 0
    
    def dfs2(u, cid):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp[node] == -1:
                comp[node] = cid
                for v in radj[node]:
                    if comp[v] == -1:
                        stack.append(v)
    
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, comp_id)
            comp_id += 1
    
    # Check for contradiction: x and not x in same SCC
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
    
    # Assign values: if comp[x] > comp[not x], set x to True
    # This means we process in reverse topological order of SCCs
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i + 1] > comp[2 * i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()