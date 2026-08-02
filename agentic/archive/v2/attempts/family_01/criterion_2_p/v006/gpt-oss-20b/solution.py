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

    color = [-1] * (n + 1)          # -1 unvisited, 0 or 1 for bipartite colors

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        color[start] = 0
        component = [start]
        ok = True
        while q:
            v = q.popleft()
            cv = color[v]
            for nb in adj[v]:
                if color[nb] == -1:
                    color[nb] = 1 - cv
                    q.append(nb)
                    component.append(nb)
                elif color[nb] == cv:
                    # not bipartite
                    print("NO")
                    return
        # ensure lexicographically smallest: make minimal index vertex have label 1
        min_idx = min(component)
        if color[min_idx] == 1:
            for v in component:
                color[v] ^= 1  # swap colors

    # Build answer
    ans = [str(color[i] + 1) for i in range(1, n + 1)]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(ans))

if __name__ == "__main__":
    solve()