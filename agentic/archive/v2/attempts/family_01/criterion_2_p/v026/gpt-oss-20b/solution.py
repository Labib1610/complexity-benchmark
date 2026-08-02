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

    color = [0] * (n + 1)  # 0 uncolored, 1 or 2
    for start in range(1, n + 1):
        if color[start]:
            continue
        # start new component, assign start = 1
        color[start] = 1
        dq = deque([start])
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu  # opposite color
                    dq.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return
    # All components bipartite
    out = ["YES\n"] + [" ".join(map(str, color[1:]))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()