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

    color = [-1] * n  # 0 or 1
    for start in range(n):
        if color[start] != -1:
            continue
        # start new component with color 0 at the smallest vertex
        dq = deque([start])
        color[start] = 0
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    dq.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    # map to frequencies
    freqs = ['1' if c == 0 else '2' for c in color]
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(freqs))

if __name__ == "__main__":
    solve()