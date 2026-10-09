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

    def lit(l: int):
        idx = abs(l) - 1
        if l > 0:          # want xi = 1
            return 2 * idx + 1, 2 * idx      # (node, neg)
        else:              # want xi = 0
            return 2 * idx, 2 * idx + 1

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        a_node, a_neg = lit(a)
        b_node, b_neg = lit(b)
        # ¬a -> b
        g[a_neg].append(b_node)
        rg[b_node].append(a_neg)
        # ¬b -> a
        g[b_neg].append(a_node)
        rg[a_node].append(b_neg)

    visited = [False] * N
    order = []

    sys.setrecursionlimit(1 << 25)
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
    cur = 0
    def rdfs(v, label):
        stack = [v]
        while stack:
            x = stack.pop()
            if comp[x] != -1:
                continue
            comp[x] = label
            for to in rg[x]:
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
        assignment[i] = 1 if comp[2*i+1] > comp[2*i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()