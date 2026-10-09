import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = n * 2
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def node(i, val):  # val 0/1 for s_i == val
        return i * 2 + val

    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        a = abs(c1) - 1
        b = abs(c2) - 1
        # value of s that makes v = 1
        # v = sign * (1-2s) == 1  => s = (sign==-1)
        val_a = 1 if c1 < 0 else 0
        val_b = 1 if c2 < 0 else 0
        # clause: (s_a != val_a) OR (s_b != val_b)
        # implications:
        # (s_a == val_a) -> (s_b == 1-val_b)
        # (s_b == val_b) -> (s_a == 1-val_a)
        u = node(a, val_a)
        v = node(b, 1 - val_b)
        g[u].append(v)
        rg[v].append(u)

        u = node(b, val_b)
        v = node(a, 1 - val_a)
        g[u].append(v)
        rg[v].append(u)

    visited = [False] * N
    order = []

    def dfs(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N

    def rdfs(v, k):
        comp[v] = k
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, k)

    k = 0
    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, k)
            k += 1

    assignment = [0] * n
    for i in range(n):
        if comp[node(i, 0)] == comp[node(i, 1)]:
            print("NO")
            return
        assignment[i] = 1 if comp[node(i, 1)] > comp[node(i, 0)] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()