import sys

sys.setrecursionlimit(1 << 25)

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
        return 2 * v if x > 0 else 2 * v + 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit_id(a)
        B = lit_id(b)
        NA = A ^ 1
        NB = B ^ 1
        g[NA].append(B)
        g[NB].append(A)
        rg[B].append(NA)
        rg[A].append(NB)

    # Kosaraju
    visited = [False] * N
    order = []

    sys.setrecursionlimit(10 ** 6)

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            v, state = stack.pop()
            if state == 0:
                if visited[v]:
                    continue
                visited[v] = True
                stack.append((v, 1))
                for to in g[v]:
                    if not visited[to]:
                        stack.append((to, 0))
            else:
                order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    cid = 0

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
            rdfs(v, cid)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()