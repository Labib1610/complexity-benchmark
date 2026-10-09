import sys
sys.setrecursionlimit(1_000_000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT: variables 0..n-1 => X_i (x_i=1)
    # negation: i+n => not X_i
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))

        # For first channel
        if c1 > 0:
            # A = X_{c1}
            A = c1 - 1
            notA = A + n
        else:
            # A = not X_{|c1|}
            notA = (-c1) - 1
            A = notA + n

        # For second channel
        if c2 > 0:
            B = c2 - 1
            notB = B + n
        else:
            notB = (-c2) - 1
            B = notB + n

        # Clause: not A or not B
        # implication: A -> not B, B -> not A
        g[A].append(notB)
        gr[notB].append(A)

        g[B].append(notA)
        gr[notA].append(B)

    # Kosaraju SCC
    visited = [False] * N
    order = []

    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Build assignment
    assignment = [False] * n
    for i in range(n):
        # If comp[i] > comp[i+n], X_i is true; else false
        assignment[i] = comp[i] > comp[i + n]

    # assignment[i] = True => x_i=1 => s_i=0
    # assignment[i] = False => x_i=-1 => s_i=1
    res = ['0' if assignment[i] else '1' for i in range(n)]
    print("YES")
    print(' '.join(res))

if __name__ == "__main__":
    solve()