import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit_id(x: int) -> int:
        v = abs(x) - 1
        return v * 2 + (0 if x > 0 else 1)   # true -> even, false -> odd

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        A = lit_id(a)
        B = lit_id(b)
        NA = A ^ 1
        NB = B ^ 1
        # ¬A -> B
        g[NA].append(B)
        rg[B].append(NA)
        # ¬B -> A
        g[NB].append(A)
        rg[A].append(NB)

    sys.setrecursionlimit(1 << 25)
    visited = [False] * N
    order = []

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            v, idx = stack[-1]
            if not visited[v]:
                visited[v] = True
            adj = g[v]
            if idx < len(adj):
                stack[-1] = (v, idx + 1)
                to = adj[idx]
                if not visited[to]:
                    stack.append((to, 0))
            else:
                order.append(v)
                stack.pop()

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    cur = 0
    def rdfs(v: int, label: int):
        stack = [v]
        while stack:
            u = stack.pop()
            if comp[u] != -1:
                continue
            comp[u] = label
            for to in rg[u]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()