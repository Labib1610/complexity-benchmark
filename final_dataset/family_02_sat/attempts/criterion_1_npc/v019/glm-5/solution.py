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
            var = abs(val) - 1
            lit = 2 * var + (1 if val > 0 else 0)
            c.append(lit)
        clauses.append(c)
    
    N = n
    total_vars = 2 * N
    
    # Build implication graph
    adj = [[] for _ in range(total_vars)]
    radj = [[] for _ in range(total_vars)]
    
    for a, b, c in clauses:
        # (a or b or c) = (a or b) and (a or c) and (b or c)
        pairs = [(a, b), (a, c), (b, c)]
        for u, v in pairs:
            nu = u ^ 1
            nv = v ^ 1
            adj[nu].append(v)
            radj[v].append(nu)
            adj[nv].append(u)
            radj[u].append(nv)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * total_vars
    order = []
    
    def dfs1(u):
        stack = [u]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            order.append(node)
            for v in adj[node]:
                if not visited[v]:
                    stack.append(v)
    
    for i in range(total_vars):
        if not visited[i]:
            dfs1(i)
    
    comp_id = [-1] * total_vars
    def dfs2(u, cid):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp_id[node] != -1:
                continue
            comp_id[node] = cid
            for v in radj[node]:
                if comp_id[v] == -1:
                    stack.append(v)
    
    cid = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    assignment = [False] * N
    for i in range(N):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
        assignment[i] = comp_id[2 * i] > comp_id[2 * i + 1]
    
    print("YES")
    print(' '.join('1' if x else '0' for x in assignment))

if __name__ == "__main__":
    solve()