import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # 0 / 1 during BFS
    answer = [0] * (n + 1)          # final frequencies 1 / 2

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS of a new component
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return
        # decide orientation: smallest index gets frequency 1
        minv = min(comp)
        flip = (color[minv] == 1)   # need to invert colours?
        for v in comp:
            final = color[v] ^ flip   # 0 -> freq 1, 1 -> freq 2
            answer[v] = 1 if final == 0 else 2

    out = ["YES"]
    out.append(' '.join(str(answer[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()