import sys
sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # 2-SAT: node index for literal x:
    # x > 0: (x-1)*2 for True, (x-1)*2+1 for False
    # We'll use: node 2*i for i True, 2*i+1 for i False
    # For literal l:
    #   if l > 0: node = 2*(l-1)
    #   if l < 0: node = 2*(-l-1)+1
    # Negation: node ^ 1
    
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    for _ in range(m):
        a, b = map(int, input().split())
        # a OR b
        # !a -> b
        # !b -> a
        def node(lit):
            if lit > 0:
                return 2 * (lit - 1)
            else:
                return 2 * (-lit - 1) + 1
        na = node(a) ^ 1
        nb = node(b) ^ 1
        add_imp(na, node(b))
        add_imp(nb, node(a))
    
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
    
    # Check contradiction
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign values: in SCC order, if comp[true] > comp[false] => true
    ans = [0] * n
    for i in range(n):
        # comp[2*i] is True literal, comp[2*i+1] is False literal
        ans[i] = 1 if comp[2*i] > comp[2*i+1] else 0
    
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()