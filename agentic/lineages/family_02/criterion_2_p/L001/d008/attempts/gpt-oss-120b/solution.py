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

    def var_node(i: int, val: int) -> int:
        # i: 0‑based hub index, val: 0 or 1 meaning x_i == val
        return i * 2 + val

    for _ in range(m):
        v1 = int(next(it))
        v2 = int(next(it))
        i1 = abs(v1) - 1
        i2 = abs(v2) - 1
        val1 = 1 if v1 < 0 else 0   # trigger when s_i == (v<0)
        val2 = 1 if v2 < 0 else 0
        # clause: NOT (s_i1 == val1 AND s_i2 == val2)
        # i.e., (s_i1 != val1) OR (s_i2 != val2)
        # literals A = (s_i1 == val1), B = (s_i2 == val2)
        A = var_node(i1, val1)
        notA = var_node(i1, 1 - val1)
        B = var_node(i2, val2)
        notB = var_node(i2, 1 - val2)
        # A -> notB
        g[A].append(notB)
        rg[notB].append(A)
        # B -> notA
        g[B].append(notA)
        rg[notA].append(B)

    order = []
    visited = [False] * N

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
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
        # higher component number = earlier in topological order
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()