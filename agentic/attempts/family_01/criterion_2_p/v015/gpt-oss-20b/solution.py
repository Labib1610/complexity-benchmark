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
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # 0 or 1
    sector = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS to color component
        queue = deque([start])
        color[start] = 0
        comp_nodes = [start]
        min_node = start
        bipartite = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                    comp_nodes.append(v)
                    if v < min_node:
                        min_node = v
                elif color[v] == color[u]:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            sys.stdout.write("NO\n")
            return
        # orientation: make min_node sector 1
        if color[min_node] == 0:
            mapping = {0: 1, 1: 2}
        else:
            mapping = {0: 2, 1: 1}
        for node in comp_nodes:
            sector[node] = mapping[color[node]]

    # output
    out_lines = ["YES", " ".join(str(sector[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()