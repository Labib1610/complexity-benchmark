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

    color = [-1] * (n + 1)   # -1 unvisited, 0 or 1
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start component with color 0
        queue = deque([start])
        color[start] = 0
        ans[start] = 1  # color 0 -> group 1
        while queue:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    ans[v] = color[v] + 1  # 0->1, 1->2
                    queue.append(v)
                elif color[v] == cu:
                    # conflict
                    sys.stdout.write("NO")
                    return
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()