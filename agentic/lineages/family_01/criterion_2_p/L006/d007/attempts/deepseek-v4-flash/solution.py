import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            q = deque([start])
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
    print(" ".join(map(str, color[1:]))))

if __name__ == "__main__":
    solve()