import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]
    
    def node(var, val):
        # var: 1-indexed variable, val: True means x, False means ¬x
        return 2 * (var - 1) + (0 if val else 1)
    
    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)
    
    for _ in range(m):
        a, b = map(int, input().split())
        # literal for probe: if positive -> x, if negative -> ¬x
        def lit_to_node(lit):
            var = abs(lit)
            val = lit > 0
            return node(var, val)
        u = lit_to_node(a)
        v = lit_to_node(b)
        # clause (u OR v) -> ¬u -> v, ¬v -> u
        add_imp(u ^ 1, v)  # u^1 flips the bit: if u is x, u^1 is ¬x
        add_imp(v ^ 1, u)
    
    # Kosaraju
    visited = [False] * N
    order = []
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            visited[i] = True
            while stack:
                v, state = stack.pop()
                if state == 0:
                    stack.append((v, 1))
                    for to in g[v]:
                        if not visited[to]:
                            visited[to] = True
                            stack.append((to, 0))
                else:
                    order.append(v)
    
    comp = [-1] * N
    def dfs_rev(v, c):
        stack = [v]
        comp[v] = c
        while stack:
            x = stack.pop()
            for to in rg[x]:
                if comp[to] == -1:
                    comp[to] = c
                    stack.append(to)
    
    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            dfs_rev(v, cid)
            cid += 1
    
    ans = [0] * n
    for i in range(1, n+1):
        x_node = node(i, True)
        nx_node = node(i, False)
        if comp[x_node] == comp[nx_node]:
            print("NO")
            return
        # In Kosaraju, comp id order: later in finishing order gets smaller comp id?
        # Actually we assign comp ids in reverse finishing order, so comp id 0 is the sink SCC.

        # For 2-SAT, if comp[x] > comp[¬x] then x = True.

        if comp[x_node] > comp[nx_node]:
            ans[i-1] = 1
        else:
            ans[i-1] = 0
    
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()