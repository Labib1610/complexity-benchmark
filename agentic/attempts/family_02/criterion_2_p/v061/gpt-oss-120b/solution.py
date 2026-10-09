import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    V = 2 * n
    adj = [[] for _ in range(V)]
    radj = [[] for _ in range(V)]

    def lit_id(x: int) -> int:
        v = abs(x) - 1
        return 2 * v if x > 0 else 2 * v + 1

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        A = lit_id(a)
        B = lit_id(b)
        NA = A ^ 1
        NB = B ^ 1
        adj[NA].append(B)
        radj[B].append(NA)
        adj[NB].append(A)
        radj[A].append(NB)

    visited = [False] * V
    order = []

    for start in range(V):
        if visited[start]:
            continue
        stack = [(start, 0)]
        visited[start] = True
        while stack:
            v, idx = stack[-1]
            if idx < len(adj[v]):
                nxt = adj[v][idx]
                stack[-1] = (v, idx + 1)
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(v)
                stack.pop()

    comp = [-1] * V
    cur = 0
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        comp[v] = cur
        while stack:
            curv = stack.pop()
            for nxt in radj[curv]:
                if comp[nxt] == -1:
                    comp[nxt] = cur
                    stack.append(nxt)
        cur += 1

    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()