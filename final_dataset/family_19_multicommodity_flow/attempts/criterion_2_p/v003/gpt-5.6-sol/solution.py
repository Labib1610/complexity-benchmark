import sys
from collections import deque

def main():
    input = sys.stdin.buffer.readline
    n, m, _ = map(int, input().split())
    s, t, demand = map(int, input().split())
    s -= 1
    t -= 1

    adj = [[] for _ in range(n)]
    to = []
    residual = []
    original_caps = []

    for _ in range(m):
        u, v, capacity = map(int, input().split())
        u -= 1
        v -= 1

        edge_id = len(to)
        to.append(v)
        residual.append(capacity)
        adj[u].append(edge_id)

        to.append(u)
        residual.append(0)
        adj[v].append(edge_id + 1)

        original_caps.append(capacity)

    if demand == 0 or s == t:
        print("YES")
        print(" ".join(["0"] * m))
        return

    sys.setrecursionlimit(max(1_000_000, 2 * n + 10))
    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            v = queue.popleft()
            next_level = level[v] + 1
            for edge_id in adj[v]:
                u = to[edge_id]
                if residual[edge_id] > 0 and level[u] == -1:
                    level[u] = next_level
                    queue.append(u)

        return level[t] != -1

    def dfs(v, pushed):
        if v == t:
            return pushed

        edges = adj[v]
        while ptr[v] < len(edges):
            edge_id = edges[ptr[v]]
            u = to[edge_id]

            if residual[edge_id] > 0 and level[u] == level[v] + 1:
                sent = dfs(u, min(pushed, residual[edge_id]))
                if sent:
                    residual[edge_id] -= sent
                    residual[edge_id ^ 1] += sent
                    return sent

            ptr[v] += 1

        return 0

    total_flow = 0

    while total_flow < demand and bfs():
        ptr[:] = [0] * n
        while total_flow < demand:
            sent = dfs(s, demand - total_flow)
            if sent == 0:
                break
            total_flow += sent

    if total_flow < demand:
        print("NO")
        return

    flows = [
        str(original_caps[i] - residual[2 * i])
        for i in range(m)
    ]

    print("YES")
    print(" ".join(flows))

if __name__ == "__main__":
    main()