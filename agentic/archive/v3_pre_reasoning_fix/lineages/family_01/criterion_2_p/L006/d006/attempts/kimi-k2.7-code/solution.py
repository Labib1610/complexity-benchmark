import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        if u != v:
            adj[v].append(u)

    color = [-1] * n
    ans = [0] * n

    for i in range(n):
        if color[i] != -1:
            continue
        dq = deque([i])
        color[i] = 0
        min_node = i
        comp_nodes = []
        while dq:
            u = dq.popleft()
            comp_nodes.append(u)
            if u < min_node:
                min_node = u
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    dq.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO")
                    return
        flip = 1 if color[min_node] == 1 else 0
        for u in comp_nodes:
            ans[u] = (color[u] ^ flip) + 1

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()