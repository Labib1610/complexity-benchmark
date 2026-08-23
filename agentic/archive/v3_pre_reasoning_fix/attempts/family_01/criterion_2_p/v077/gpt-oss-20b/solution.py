import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # -1 unvisited, 0 or 1
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for this component
        dq = deque([start])
        color[start] = 0
        while dq:
            u = dq.popleft()
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    dq.append(w)
                elif color[w] == color[u]:
                    sys.stdout.write("NO")
                    return

    # Assign frequencies: 0 -> 1, 1 -> 2
    for i in range(1, n + 1):
        ans[i] = 1 if color[i] == 0 else 2

    out_lines = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()