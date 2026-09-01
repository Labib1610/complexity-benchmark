import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
    
    # For each edge (u,v), M_u->v = s_u*v + s_v*u, M_v->u = s_v*v + s_u*u
    # Equality when s_u*(v-u) == s_v*(v-u), i.e. s_u == s_v (since u != v)
    # So constraint: s_u != s_v for every edge.
    # We need 3-coloring of graph, minimizing signature V_n = base-4 value of s_1..s_n.
    # Minimize lexicographically s_1, s_2, ..., s_n (since 1,2,3 < 4).
    
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0]*(n+1)
    
    def feasible(i, c):
        for w in adj[i]:
            if color[w] == c:
                return False
        return True
    
    def backtrack(i):
        if i > n:
            return True
        for c in (1, 2, 3):
            if feasible(i, c):
                color[i] = c
                if backtrack(i+1):
                    return True
        color[i] = 0
        return False
    
    if backtrack(1):
        out = ['YES']
        out.append(' '.join(str(color[i]) for i in range(1, n+1)))
        sys.stdout.write('\n'.join(out) + '\n')
    else:
        sys.stdout.write('NO\n')

solve()