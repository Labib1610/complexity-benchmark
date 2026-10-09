import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    # 2-SAT: nodes 0..2n-1
    # node 2*i = x_i = 1
    # node 2*i+1 = x_i = 0
    g = [[] for _ in range(2*n)]
    gr = [[] for _ in range(2*n)]
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    for _ in range(m):
        l1, l2 = map(int, input().split())
        a = abs(l1) - 1
        b = abs(l2) - 1
        # m1 node
        if l1 > 0:
            m1 = 2*a + 1  # x_a = 0
        else:
            m1 = 2*a      # x_a = 1
        # m2 node
        if l2 > 0:
            m2 = 2*b + 1
        else:
            m2 = 2*b
        # m1 -> ¬m2
        add_imp(m1, m2 ^ 1)
        # m2 -> ¬m1
        add_imp(m2, m1 ^ 1)
    
    # Kosaraju
    visited = [False]*(2*n)
    order = []
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2*n):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1]*(2*n)
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
    
    # Assign values: choose the one with higher comp id (topological order)
    val = [0]*n
    for i in range(n):
        # comp[2*i] is x_i=1, comp[2*i+1] is x_i=0
        # In Kosaraju, comp id order is reverse topological
        # So if comp[2*i] > comp[2*i+1], set x_i=1 else 0
        if comp[2*i] > comp[2*i+1]:
            val[i] = 1
        else:
            val[i] = 0
    
    print("YES")
    print(" ".join(map(str, val)))

if __name__ == "__main__":
    solve()