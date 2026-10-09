import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 2*i for False, 2*i+1 for True

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # literal to node index
        def node(lit):
            var = abs(lit) - 1
            return 2 * var + (1 if lit > 0 else 0)
        u = node(a)
        v = node(b)
        # (not u) -> v
        add_imp(u ^ 1, v)
        # (not v) -> u
        add_imp(v ^ 1, u)

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
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # Build assignment: choose value based on SCC order
    assignment = [0] * n
    for i in range(n):
        # If True node has higher comp id, set True
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()