import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    color = [0] * (n + 1)          # 0 = unvisited, 1 or -1 = two sides
    answer = [0] * (n + 1)         # final band (1 or 2)

    for start in range(1, n + 1):
        if color[start]:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 1
        comp_nodes = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not color[v]:
                    color[v] = -color[u]
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide which side gets band 1
        # find smallest index vertex in component
        min_vertex = min(comp_nodes)
        # side of that vertex gets band 1
        side_one = color[min_vertex]   # 1 or -1
        for v in comp_nodes:
            answer[v] = 1 if color[v] == side_one else 2

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()