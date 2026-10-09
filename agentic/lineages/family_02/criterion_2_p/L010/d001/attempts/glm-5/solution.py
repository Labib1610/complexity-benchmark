import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Implication graph has 2*n nodes: 0..n-1 are False, n..2n-1 are True
    # Node index: x*1 for False, x*n+1 for True (using 0-based switch index)
    # Actually, let's use: 2*x for False, 2*x+1 for True
    size = 2 * n
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        
        # Determine the state that is "safe" (s_i)
        # If l_i > 0, safe is ON (1). If l_i < 0, safe is OFF (0).
        s_u = 1 if l1 > 0 else 0
        s_v = 1 if l2 > 0 else 0
        
        # The forbidden condition is: (u is !s_u) AND (v is !s_v)
        # This translates to two implications:
        # 1. If u is !s_u, then v must be s_v.
        # 2. If v is !s_v, then u must be s_u.
        
        # Node indices:
        # 2*u for u=False(0), 2*u+1 for u=True(1)
        # We need to map states to indices.
        
        # Implication 1: (u == !s_u) -> (v == s_v)
        u_from1 = 2*u + (1 - s_u)
        v_to1 = 2*v + s_v
        adj[u_from1].append(v_to1)
        radj[v_to1].append(u_from1)
        
        # Implication 2: (v == !s_v) -> (u == s_u)
        v_from2 = 2*v + (1 - s_v)
        u_to2 = 2*u + s_u
        adj[v_from2].append(u_to2)
        radj[u_to2].append(v_from2)

    # Kosaraju's algorithm for SCC
    visited = [False] * size
    order = []
    
    def dfs1(u):
        stack = [u]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                stack.append(v) # push back to process children after
                for w in adj[v]:
                    if not visited[w]:
                        stack.append(w)
        order.append(u)

    for i in range(size):
        if not visited[i]:
            dfs1(i)
            
    comp_id = [-1] * size
    cid = 0
    
    def dfs2(u, cid):
        stack = [u]
        while stack:
            v = stack.pop()
            if comp_id[v] == -1:
                comp_id[v] = cid
                for w in radj[v]:
                    if comp_id[w] == -1:
                        stack.append(w)

    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, cid)
            cid += 1
            
    assignment = [0] * n
    possible = True
    
    for i in range(n):
        if comp_id[2*i] == comp_id[2*i+1]:
            possible = False
            break
        # If True component is processed later (higher topological order),
        # it is "better" (can be set to True).
        assignment[i] = 1 if comp_id[2*i+1] > comp_id[2*i] else 0

    if not possible:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assignment)) + "\n")

if __name__ == '__main__':
    solve()