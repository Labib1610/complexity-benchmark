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

    color = [-1] * (n + 1)          # -1 unvisited, 0 or 1 otherwise
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start new component, force start vertex to color 0 (=> vault 1)
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    # construct answer: vault numbers are color+1
    ans = ' '.join(str(c + 1) for c in color[1:])
    sys.stdout.write("YES\n")
    sys.stdout.write(ans)

if __name__ == "__main__":
    solve()