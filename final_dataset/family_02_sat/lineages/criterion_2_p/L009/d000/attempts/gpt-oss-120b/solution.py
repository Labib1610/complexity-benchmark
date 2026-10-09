import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = n * 2
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit_to_node(l: int) -> int:
        if l > 0:
            v = l - 1
            return v * 2      # true
        else:
            v = -l - 1
            return v * 2 + 1  # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        na = lit_to_node(-a)
        nb = lit_to_node(-b)
        a_node = lit_to_node(a)
        b_node = lit_to_node(b)
        # ¬a -> b
        g[na].append(b_node)
        rg[b_node].append(na)
        # ¬b -> a
        g[nb].append(a_node)
        rg[a_node].append(nb)

    visited = [False] * N
    order = []

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            v, idx = stack.pop()
            if idx == 0:
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

    def rdfs(v: int, cid: int):
        stack = [v]
        while stack:
            v = stack.pop()
            if comp[v] != -1:
                continue
            comp[v] = cid
            for to in rg[v]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

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