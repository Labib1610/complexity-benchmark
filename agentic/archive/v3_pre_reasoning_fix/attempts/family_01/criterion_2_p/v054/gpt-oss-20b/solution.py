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

    color = [-1] * (n + 1)          # 0 or 1
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for component
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return
        # lexicographically minimal: ensure smallest node gets color 0
        min_node = min(comp)
        if color[min_node] == 1:
            for v in comp:
                color[v] ^= 1

    # All components processed
    out = ["YES"]
    seq = [str(color[i] + 1) for i in range(1, n + 1)]
    out.append(" ".join(seq))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()