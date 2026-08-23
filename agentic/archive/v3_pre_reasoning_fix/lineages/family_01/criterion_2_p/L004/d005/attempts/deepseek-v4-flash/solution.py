import sys
from collections import deque

def solve():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            q = deque([i])

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return

    print("YES")
    print(" ".join(map(str, color[1:])))

if __name__ == "__main__":
    solve()