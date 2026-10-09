import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    clauses = []
    for _ in range(m):
        c = []
        for _ in range(3):
            val = int(next(it))
            if val > 0:
                # x_i = True -> warm (1)
                lit = (val - 1) * 2
            else:
                # x_i = False -> cool (0)
                lit = (-val - 1) * 2 + 1
            c.append(lit)
        clauses.append(c)
    
    N = n * 2
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    for a, b, c in clauses:
        # (a OR b OR c) = (a) OR (b OR c) = (a) OR (b) OR (c)
        # Decompose into implications
        # not a -> b, not a -> c
        # not b -> a, not b -> c
        # not c -> a, not c -> b
        na = a ^ 1
        nb = b ^ 1
        nc = c ^ 1
        
        adj[na].append(b)
        adj[na].append(c)
        adj[nb].append(a)
        adj[nb].append(c)
        adj[nc].append(a)
        adj[nc].append(b)
        
        radj[b].append(na)
        radj[c].append(na)
        radj[a].append(nb)
        radj[c].append(nb)
        radj[a].append(nc)
        radj[b].append(nc)
    
    # Kosaraju's algorithm
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                nei = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[nei]:
                    stack.append((nei, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    def dfs2(u, c):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = c
            for nei in radj[node]:
                if comp[nei] == -1:
                    stack.append(nei)
    
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check 2-SAT validity
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign values
    assignment = [False] * n
    for i in range(n):
        assignment[i] = comp[2*i] > comp[2*i+1]
    
    print("YES")
    print(' '.join('1' if assignment[i] else '0' for i in range(n)))

if __name__ == "__main__":
    solve()