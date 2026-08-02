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
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)      # 0 or 1
    result = [0] * (n + 1)      # 1 or 2

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return
        # assign vault numbers: 0 -> 1, 1 -> 2
        for v in comp:
            result[v] = color[v] + 1

    out_lines = ["YES", " ".join(str(result[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()