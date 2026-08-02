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

    color = [0] * (n + 1)  # 0 = uncolored, 1 or 2

    for start in range(1, n + 1):
        if color[start]:
            continue
        # BFS for this component, assign start color 1
        queue = deque([start])
        color[start] = 1
        while queue:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if not color[v]:
                    color[v] = 3 - cu
                    queue.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(color[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n')

if __name__ == "__main__":
    solve()