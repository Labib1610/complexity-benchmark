import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(lit):
        # lit: positive -> high-gain, negative -> low-gain
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var      # high-gain true
        else:
            return 2 * var + 1  # low-gain true

    def neg_node(idx):
        return idx ^ 1

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # clause (a OR b) => (!a -> b) and (!b -> a)
        g[neg_node(u)].append(v)
        g[neg_node(v)].append(u)
        gr[v].append(neg_node(u))
        gr[u].append(neg_node(v))

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

    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    print("YES")
    ans = []
    for i in range(n):
        # If high-gain node's component is after low-gain's, set high-gain
        if comp[2*i] > comp[2*i+1]:
            ans.append('1')
        else:
            ans.append('0')
    print(' '.join(ans))

if __name__ == "__main__":
    main()