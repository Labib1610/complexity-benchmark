import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS to collect component
        comp_nodes = []
        q = deque([start])
        color[start] = 0
        comp_nodes.append(start)
        bip = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    comp_nodes.append(v)
                    q.append(v)
                elif color[v] == color[u]:
                    bip = False
                    break
            if not bip:
                break
        if not bip:
            print("NO")
            return

        # Determine orientation for lexicographically smallest
        min_node = min(comp_nodes)
        flip = 0
        if color[min_node] == 1:
            flip = 1
        for node in comp_nodes:
            ans[node] = 1 + (color[node] ^ flip)

    print("YES")
    print(' '.join(map(str, ans[1:])))

if __name__ == "__main__":
    solve()