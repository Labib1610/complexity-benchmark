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

    def lit_to_node(x: int) -> int:
        v = abs(x) - 1
        if x > 0:
            return v * 2 + 1   # true
        else:
            return v * 2       # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit_to_node(a)
        B = lit_to_node(b)
        NA = A ^ 1
        NB = B ^ 1
        # ¬A -> B
        g[NA].append(B)
        rg[B].append(NA)
        # ¬B -> A
        g[NB].append(A)
        rg[A].append(NB)

    visited = [False] * N
    order = []

    sys.setrecursionlimit(1 << 25)

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))  # post
                for to in g[node]:
                    if not visited[to]:
                        stack.append((to, 0))
            else:
                order.append(node)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    cid = 0

    def rdfs(v: int, label: int):
        stack = [v]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = label
            for to in rg[node]:
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
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()