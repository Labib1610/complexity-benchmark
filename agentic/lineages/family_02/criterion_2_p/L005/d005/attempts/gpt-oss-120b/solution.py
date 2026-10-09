import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of nodes in implication graph
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        # first literal
        i1 = abs(l1) - 1
        sign1 = 1 if l1 > 0 else -1
        f1 = 1 if sign1 == -1 else 0          # forbidden value of v_i
        # we need (v_i != f) -> literal A
        litA = 2 * i1 + (0 if f1 == 0 else 1)  # true if f==0 else false
        # second literal
        i2 = abs(l2) - 1
        sign2 = 1 if l2 > 0 else -1
        f2 = 1 if sign2 == -1 else 0
        litB = 2 * i2 + (0 if f2 == 0 else 1)

        # clause (litA OR litB)
        notA = litA ^ 1
        notB = litB ^ 1
        add_imp(notA, litB)
        add_imp(notB, litA)

    # Kosaraju
    visited = [False] * N
    order = []

    def dfs(v):
        stack = [v]
        while stack:
            node = stack[-1]
            if visited[node]:
                stack.pop()
                continue
            visited[node] = True
            for to in g[node]:
                if not visited[to]:
                    stack.append(to)
            # after exploring children, record order
            if stack[-1] == node:
                stack.pop()
                order.append(node)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    label = 0
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = label
            while stack:
                node = stack.pop()
                for to in rg[node]:
                    if comp[to] == -1:
                        comp[to] = label
                        stack.append(to)
            label += 1

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