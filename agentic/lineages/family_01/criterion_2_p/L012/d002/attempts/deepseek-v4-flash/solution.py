from sys import stdin
from collections import deque

def solve():
    input_data = stdin.read().split()
    n, m = int(input_data[0]), int(input_data[1])
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    color = [-1] * n

    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return

    print("YES")
    print(" ".join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()