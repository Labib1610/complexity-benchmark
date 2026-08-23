import sys
from collections import deque

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    try:
        n = next(it)
    except StopIteration:
        return
    m = next(it)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    for i in range(n):
        if color[i] != -1:
            continue

        color[i] = 0
        q = deque([i])

        while q:
            u = q.popleft()
            expected = 1 - color[u]

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = expected
                    q.append(v)
                elif color[v] != expected:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(c + 1) for c in color) + "\n")

if __name__ == "__main__":
    main()