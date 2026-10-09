import sys
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    graph = [[] for _ in range(N)]
    rev_graph = [[] for _ in range(N)]

    def node(var):
        # var > 0: valve var = 1 (bypass)
        # var < 0: valve -var = 0 (radiator)
        if var > 0:
            return (var - 1) * 2 + 1
        else:
            return (-var - 1) * 2

    def add_imp(u, v):
        graph[u].append(v)
        rev_graph[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # clause (a or b) => (!a -> b) and (!b -> a)
        add_imp(node(-a), node(b))
        add_imp(node(-b), node(a))

    # Kosaraju's SCC
    visited = [False] * N
    order = []

    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for v in rev_graph[u]:
            if comp[v] == -1:
                dfs2(v, cid)

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

    # Assign values
    assignment = [0] * n
    for i in range(n):
        # If comp[2*i] > comp[2*i+1], set True (1), else False (0)
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()