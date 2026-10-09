import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        c1, c2 = map(int, input().split())
        # parameter is 1 if:
        # c>0: x[|c|] is True
        # c<0: x[|c|] is False
        # So literal for "param is 1":
        lit1 = c1 > 0
        lit2 = c2 > 0
        var1 = abs(c1) - 1
        var2 = abs(c2) - 1
        # clause: (lit1 ? x_var1 : ~x_var1) OR (lit2 ? x_var2 : ~x_var2)
        # In 2-SAT: (a OR b) => (~a -> b) and (~b -> a)
        # a is True if lit1 is True and var1 is True, or lit1 False and var1 False.
        # So a = (lit1 == x_var1)
        # ~a = (lit1 != x_var1)
        # We'll encode node for each literal: 2*var for False, 2*var+1 for True
        # a_lit = 2*var1 + (1 if lit1 else 0)
        # b_lit = 2*var2 + (1 if lit2 else 0)
        a_lit = 2 * var1 + (1 if lit1 else 0)
        b_lit = 2 * var2 + (1 if lit2 else 0)
        # ~a_lit = a_lit ^ 1
        # ~b_lit = b_lit ^ 1
        clauses.append((a_lit, b_lit))
    
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    for a, b in clauses:
        # ~a -> b
        g[a ^ 1].append(b)
        gr[b].append(a ^ 1)
        # ~b -> a
        g[b ^ 1].append(a)
        gr[a].append(b ^ 1)
    
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
    
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    print("YES")
    res = []
    for i in range(n):
        # If comp[2*i] > comp[2*i+1] means False literal is later in topological order => assign True
        # Standard: if comp[2*i] > comp[2*i+1] then x_i = True
        if comp[2*i] > comp[2*i+1]:
            res.append('1')
        else:
            res.append('0')
    print(' '.join(res))

if __name__ == "__main__":
    solve()