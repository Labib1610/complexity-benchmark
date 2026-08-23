import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != 0:
            continue

        color[start] = 1
        q = deque([start])

        while q:
            u = q.popleft()
            next_color = 2 if color[u] == 1 else 1

            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_color
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return

    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()