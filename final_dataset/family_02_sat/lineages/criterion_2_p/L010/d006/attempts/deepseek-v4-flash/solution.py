import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # 2-SAT: variables 1..n, each variable i has two nodes: 2*i (false) and 2*i+1 (true)
    # We'll use 0-indexed: node 2*i = false, 2*i+1 = true
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    def add_clause(a, b):
        # clause (a OR b), where a,b are literals
        # literal: (var, is_true) where var in 0..n-1
        # node for literal: 2*var + (1 if is_true else 0)
        # negation: 2*var + (0 if is_true else 1)
        def node(lit):
            var, val = lit
            return 2*var + (1 if val else 0)
        def neg(lit):
            var, val = lit
            return (var, not val)
        # (a OR b) == (~a -> b) and (~b -> a)
        add_imp(node(neg(a)), node(b))
        add_imp(node(neg(b)), node(a))
    
    for _ in range(m):
        l1, l2 = map(int, input().split())
        a = abs(l1) - 1
        b = abs(l2) - 1
        s1 = 1 if l1 > 0 else -1
        s2 = 1 if l2 > 0 else -1
        B = (s1 + s2) / 2
        
        # Check all 4 assignments
        for v1 in (0, 1):
            for v2 in (0, 1):
                R = v1 * s1 + v2 * s2
                if R < B:
                    # invalid: forbid (v1, v2)
                    # clause: (v1 != val1) OR (v2 != val2)
                    # i.e., (v1 == 1-val1) OR (v2 == 1-val2)
                    lit1 = (a, 1 - v1)
                    lit2 = (b, 1 - v2)
                    add_clause(lit1, lit2)
    
    # Kosaraju SCC
    visited = [False] * N
    order = []
    def dfs1(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs1(w)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for w in gr[u]:
            if comp[w] == -1:
                dfs2(w, cid)
    
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Build assignment
    assignment = [False] * n
    for i in range(n):
        # In Kosaraju, comp id order: if comp[2*i] > comp[2*i+1] then true
        assignment[i] = comp[2*i] > comp[2*i+1]
    
    print("YES")
    print(' '.join('1' if assignment[i] else '0' for i in range(n)))

if __name__ == "__main__":
    solve()