import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT: each variable i (1..n) has two nodes: 2*i for True, 2*i+1 for False
    N = 2 * n + 2
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    def node(var, val):
        # var: channel number, val: expected value (0 or 1)
        # returns node index for literal (var == val)
        if val == 1:
            return 2 * var
        else:
            return 2 * var + 1
    
    def neg(node_idx):
        return node_idx ^ 1
    
    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        c3 = int(next(it))
        
        # literals
        lits = []
        for c in (c1, c2, c3):
            var = abs(c)
            expected = 1 if c > 0 else 0
            lits.append(node(var, expected))
        
        # add implications for (l1 OR l2 OR l3)
        a, b, c = lits
        add_imp(neg(a), b)
        add_imp(neg(a), c)
        add_imp(neg(b), a)
        add_imp(neg(b), c)
        add_imp(neg(c), a)
        add_imp(neg(c), b)
    
    # Kosaraju SCC
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v, cid)
    
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    for i in range(1, n+1):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * (n+1)
    for i in range(1, n+1):
        # If comp[2*i] > comp[2*i+1], set True (1), else False (0)
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

if __name__ == "__main__":
    solve()