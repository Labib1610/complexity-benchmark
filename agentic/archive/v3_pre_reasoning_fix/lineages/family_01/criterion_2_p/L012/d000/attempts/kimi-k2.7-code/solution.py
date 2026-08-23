import sys
from collections import deque

def solve() -> None:
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
        adj[v].append(u)

    color = [-1] * n  # 0 or 1, output as 1 or 2

    for i in range(n):
        if color[i] != -1:
            continue
        # Start BFS from the smallest unvisited vertex in this component.
        color[i] = 0
        dq = deque([i])
        while dq:
            cur = dq.popleft()
            c = color[cur]
            for nb in adj[cur]:
                if color[nb] == -1:
                    color[nb] = c ^ 1
                    dq.append(nb)
                elif color[nb] == c:
                    print("NO")
                    return

    print("YES")
    print(' '.join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()