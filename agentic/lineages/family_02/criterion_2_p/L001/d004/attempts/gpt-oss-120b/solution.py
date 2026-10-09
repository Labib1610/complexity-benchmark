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

    def var(i):  # i from 1..n, returns index of xi true
        return (i - 1) << 1

    def neg(x):
        return x ^ 1

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        # literal true when P(|l|)=R(l)
        # map to node index
        if l1 > 0:
            a = var(l1)          # xi
        else:
            a = neg(var(-l1))    # ¬xi
        if l2 > 0:
            b = var(l2)
        else:
            b = neg(var(-l2))
        # clause (a OR b) => (¬a -> b) and (¬b -> a)
        na = neg(a)
        nb = neg(b)
        g[na].append(b)
        g[nb].append(a)
        rg[b].append(na)
        rg[a].append(nb)

    visited = [False] * N
    order = []

    def dfs(v):
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
    def rdfs(v, label):
        stack = [v]
        while stack:
            v = stack.pop()
            if comp[v] != -1:
                continue
            comp[v] = label
            for to in rg[v]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

    assignment = [0] * n
    for i in range(1, n + 1):
        if comp[var(i)] == comp[neg(var(i))]:
            print("NO")
            return
        assignment[i - 1] = 1 if comp[var(i)] > comp[neg(var(i))] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()