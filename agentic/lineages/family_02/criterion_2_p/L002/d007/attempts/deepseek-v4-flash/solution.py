import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(2 * n)]
    
    # Each variable i has two nodes: 2*i for False(0), 2*i+1 for True(1)
    # Clause: NOT (c1<0 and c2<0) => (c1>=0 OR c2>=0)
    # For c1: if c1>0, literal is (x=1); if c1<0, literal is (x=0)
    # Clause (a OR b) => (!a -> b) and (!b -> a)
    
    for _ in range(m):
        c1, c2 = map(int, input().split())
        # literal1: if c1>0 => (x=1) node 2*abs(c1)+1 ; if c1<0 => (x=0) node 2*abs(c1)
        lit1 = 2 * abs(c1) + (1 if c1 > 0 else 0)
        lit2 = 2 * abs(c2) + (1 if c2 > 0 else 0)
        # !lit1 -> lit2
        adj[lit1 ^ 1].append(lit2)
        # !lit2 -> lit1
        adj[lit2 ^ 1].append(lit1)
    
    # Kosaraju SCC
    N = 2 * n
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
    
    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for v in radj[u]:
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
        # If comp[2*i] > comp[2*i+1], then x=True (1), else False (0)
        if comp[2*i] > comp[2*i+1]:
            res.append('1')
        else:
            res.append('0')
    print(' '.join(res))

if __name__ == "__main__":
    solve()