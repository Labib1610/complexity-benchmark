import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # node count
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit(idx, val):
        """return node number for literal s_idx == val (val 0/1)"""
        # node for true (s=1) is 2*idx, false (s=0) is 2*idx+1
        # we map: true -> 2*idx, false -> 2*idx+1
        return 2 * idx + (0 if val else 1)

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        i1 = abs(l1) - 1
        i2 = abs(l2) - 1
        val1 = 0 if l1 > 0 else 1   # L(l) true when s_i == val
        val2 = 0 if l2 > 0 else 1
        a = lit(i1, val1)           # literal L(l1)
        b = lit(i2, val2)           # literal L(l2)
        na = a ^ 1                  # negation node (toggle last bit)
        nb = b ^ 1
        # clause ¬a ∨ ¬b  => a -> ¬b , b -> ¬a
        add_imp(a, nb)
        add_imp(b, na)

    # Kosaraju
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
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        comp[v] = cid
        while stack:
            x = stack.pop()
            for to in rg[x]:
                if comp[to] == -1:
                    comp[to] = cid
                    stack.append(to)
        cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        # component with larger number appears earlier in topological order
        assignment[i] = 0 if comp[2*i] > comp[2*i+1] else 1

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()