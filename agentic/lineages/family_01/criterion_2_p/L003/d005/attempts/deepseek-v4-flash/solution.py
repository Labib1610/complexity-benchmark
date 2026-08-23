import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    def bfs(start, first_color):
        # Try coloring with start = first_color
        c = color[:]
        c[start] = first_color
        q = deque([start])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if c[v] == -1:
                    c[v] = 1 - c[u]
                    q.append(v)
                elif c[v] == c[u]:
                    ok = False
                    break
            if not ok:
                break
        return ok, c

    for i in range(n):
        if color[i] == -1:
            # Try 1 first
            ok1, c1 = bfs(i, 1)
            if ok1:
                color = c1
            else:
                ok2, c2 = bfs(i, 0)
                if not ok2:
                    print("NO")
                    return
                color = c2

    print("YES")
    print(' '.join(str(x + 1) for x in color))

if __name__ == "__main__":
    solve()