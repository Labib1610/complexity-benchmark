import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS to color component
        color[start] = 0
        q = deque([start])
        comp_nodes = []
        while q:
            u = q.popleft()
            comp_nodes.append(u)
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # Now we have coloring 0/1 in this component
        # We need to decide if we flip this component to make lexicographically smallest
        # Find min index in component
        min_node = min(comp_nodes)
        if color[min_node] == 1:
            # flip colors in this component
            for node in comp_nodes:
                color[node] = 1 - color[node]

    # Output
    ans = [1 if c == 0 else 2 for c in color]
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()