import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # each variable has two nodes: 2*i for false, 2*i+1 for true

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    # node mapping: literal x -> node
    # positive v: (v-1)*2 + 1  (true)
    # negative v: (-v-1)*2     (false)
    def node(lit):
        if lit > 0:
            return (lit - 1) * 2 + 1
        else:
            return (-lit - 1) * 2

    def neg_node(lit):
        if lit > 0:
            return (lit - 1) * 2
        else:
            return (-lit - 1) * 2 + 1

    for _ in range(m):
        a, b = map(int, input().split())
        # clause (a or b) => (!a -> b) and (!b -> a)
        add_imp(neg_node(a), node(b))
        add_imp(neg_node(b), node(a))

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

    # check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # assignment: if comp[true] > comp[false] then true
    ans = []
    for i in range(n):
        if comp[2*i+1] > comp[2*i]:
            ans.append('1')
        else:
            ans.append('0')

    print("YES")
    print(" ".join(ans))

if __name__ == "__main__":
    main()