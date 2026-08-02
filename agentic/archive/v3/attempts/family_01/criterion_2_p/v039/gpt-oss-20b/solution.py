import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    color = [0] * n          # provisional bipartite colors 0/1
    lab = [0] * n            # final lab numbers 1/2

    for start in range(n):
        if visited[start]:
            continue
        stack = [start]
        visited[start] = True
        color[start] = 0
        comp = [start]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = color[u] ^ 1
                    stack.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        min_node = min(comp)
        flip = (color[min_node] == 1)
        for node in comp:
            lab[node] = (color[node] ^ flip) + 1

    print("YES")
    print(' '.join(map(str, lab)))

if __name__ == "__main__":
    solve()