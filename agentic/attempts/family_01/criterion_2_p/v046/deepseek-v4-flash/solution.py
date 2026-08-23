from collections import deque
import sys

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
    
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0  # try to start with 1 (0-indexed = 0 -> output 1)
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()