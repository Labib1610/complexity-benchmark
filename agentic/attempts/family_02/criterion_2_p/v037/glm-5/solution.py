import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    N = 2 * n + 1
    head = [-1] * N
    to = []
    nxt = []
    idx = 2
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        # (not a) -> b, (not b) -> a
        na = a ^ 1
        nb = b ^ 1
        to.append(b); nxt.append(head[na]); head[na] = len(to)-1
        to.append(a); nxt.append(head[nb]); head[nb] = len(to)-1

    visited = [0] * N
    order = []
    def dfs1(u):
        stack = [(u, False)]
        while stack:
            v, processed = stack.pop()
            if processed:
                if visited[v] != 1:
                    visited[v] = 1
                    order.append(v)
                continue
            if visited[v]:
                continue
            visited[v] = 1
            stack.append((v, True))
            e = head[v]
            while e != -1:
                w = to[e]
                if not visited[w]:
                    stack.append((w, False))
                e = nxt[e]

    for i in range(2, N):
        if not visited[i]:
            dfs1(i)

    head_r = [-1] * N
    to_r = []
    nxt_r = []
    for u in range(2, N):
        e = head[u]
        while e != -1:
            v = to[e]
            to_r.append(u); nxt_r.append(head_r[v]); head_r[v] = len(to_r)-1
            e = nxt[e]

    comp = [-1] * N
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            stack = [u]
            comp[u] = cid
            while stack:
                v = stack.pop()
                e = head_r[v]
                while e != -1:
                    w = to_r[e]
                    if comp[w] == -1:
                        comp[w] = cid
                        stack.append(w)
                    e = nxt_r[e]
            cid += 1

    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        pos = 2 * i
        neg = 2 * i + 1
        if comp[pos] == comp[neg]:
            print("NO")
            return
        assignment[i] = 1 if comp[pos] > comp[neg] else 0

    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

solve()