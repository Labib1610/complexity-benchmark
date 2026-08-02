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
        if u == v:  # self-loop, impossible
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS to color component
        q = deque([start])
        color[start] = 0
        comp = [start]
        bipartite = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            print("NO")
            return

        comp.sort()
        # Build color lists
        colors0 = [color[v] for v in comp]          # original
        colors1 = [1 - c for c in colors0]          # flipped

        # Choose orientation
        orientation = 0  # 0 -> colors0, 1 -> colors1
        for c0, c1 in zip(colors0, colors1):
            if c0 < c1:
                orientation = 0
                break
            elif c0 > c1:
                orientation = 1
                break
        # Assign modes (1 or 2)
        if orientation == 0:
            for v, c in zip(comp, colors0):
                ans[v] = c + 1
        else:
            for v, c in zip(comp, colors1):
                ans[v] = c + 1

    print("YES")
    print(' '.join(map(str, ans[1:])))

if __name__ == "__main__":
    solve()