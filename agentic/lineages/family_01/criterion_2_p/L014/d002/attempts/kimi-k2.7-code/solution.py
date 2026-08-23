import sys
from collections import deque

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    comp = [-1] * n
    min_in_comp = []

    for start in range(n):
        if color[start] != -1:
            continue
        dq = deque([start])
        color[start] = 0
        comp[start] = len(min_in_comp)
        minv = start
        while dq:
            v = dq.popleft()
            if v < minv:
                minv = v
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = 1 - color[v]
                    comp[w] = comp[start]
                    dq.append(w)
                elif color[w] == color[v]:
                    print("NO")
                    return
        min_in_comp.append(minv)

    out = []
    for i in range(n):
        cid = comp[i]
        target = color[min_in_comp[cid]]
        out.append('1' if color[i] == target else '2')

    print("YES")
    print(' '.join(out))

if __name__ == "__main__":
    solve()