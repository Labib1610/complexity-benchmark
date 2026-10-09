import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        
        u = abs(c1) - 1
        v = abs(c2) - 1
        su = 1 if c1 > 0 else 0
        sv = 1 if c2 > 0 else 0
        
        nu = 2 * u + su
        nv = 2 * v + sv
        
        adj[nu ^ 1].append(nv)
        adj[nv ^ 1].append(nu)
    
    N = 2 * n
    order = []
    visited = [False] * N
    
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                while idx < len(adj[node]) and visited[adj[node][idx]]:
                    idx += 1
                if idx < len(adj[node]):
                    stack[-1] = (node, idx + 1)
                    nxt = adj[node][idx]
                    if not visited[nxt]:
                        stack.append((nxt, 0))
                else:
                    stack.pop()
                    order.append(node)
    
    comp = [-1] * N
    comp_id = 0
    
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
    
    for u in reversed(order):
        if comp[u] == -1:
            stack = [u]
            comp[u] = comp_id
            while stack:
                node = stack.pop()
                for prev in radj[node]:
                    if comp[prev] == -1:
                        comp[prev] = comp_id
                        stack.append(prev)
            comp_id += 1
    
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()