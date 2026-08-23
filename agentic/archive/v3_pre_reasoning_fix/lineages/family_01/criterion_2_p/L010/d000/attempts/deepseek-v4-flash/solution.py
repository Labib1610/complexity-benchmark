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
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    possible = True

    for i in range(1, n + 1):
        if color[i] != -1:
            continue

        color[i] = 0
        q = deque([i])

        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    possible = False
                    break
            if not possible:
                break

        if not possible:
            break

    if not possible:
        sys.stdout.write("NO\n")
    else:
        ans = " ".join(str(c + 1) for c in color[1:])
        sys.stdout.write("YES\n" + ans + "\n")


if __name__ == "__main__":
    solve()