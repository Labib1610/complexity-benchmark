import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    color = [0] * m
    visited = [False] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack = [(start, 0, -1, -1)]
        visited[start] = True
        while stack:
            node, parity, pedge, pnode = stack.pop()
            for nb, eid in adj[node]:
                if eid == pedge:
                    continue
                if not visited[nb]:
                    visited[nb] = True
                    color[eid] = 1 + (parity ^ 1)
                    stack.append((nb, parity ^ 1, eid, node))
                else:
                    if color[eid] == 0:
                        color[eid] = 1 + parity

    for u in range(1, n + 1):
        cnt = [0, 0, 0, 0]
        for _, eid in adj[u]:
            cnt[color[eid]] += 1
        if cnt[1] != 1 or cnt[2] != 1 or cnt[3] != 1:
            print("NO")
            return

    print("YES")
    print(' '.join(map(str, color)))

solve()