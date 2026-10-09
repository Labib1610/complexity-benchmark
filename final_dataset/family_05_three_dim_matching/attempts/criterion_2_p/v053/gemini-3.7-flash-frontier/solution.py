import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    adj = [[] for _ in range(k + 1)]
    tag_of_u = [0] * (k + 1)

    idx = 2
    for _ in range(t):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3
        tag_of_u[u] = v
        adj[u].append(w)

    # Check if all containers have a tag assigned
    for u in range(1, k + 1):
        if tag_of_u[u] == 0:
            print("NO")
            return

    # Hopcroft-Karp algorithm for maximum bipartite matching
    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    dist = [0] * (k + 1)
    INF = 10**9

    # Greedy initial matching
    matching_size = 0
    for u in range(1, k + 1):
        for v in adj[u]:
            if pair_v[v] == 0:
                pair_u[u] = v
                pair_v[v] = u
                matching_size += 1
                break

    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF

        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                d = dist[u] + 1
                for v in adj[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = d
                        queue.append(pu)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            d = dist[u] + 1
            for v in adj[u]:
                pu = pair_v[v]
                if dist[pu] == d:
                    if dfs(pu):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching_size += 1

    if matching_size == k:
        out = ["YES"]
        for u in range(1, k + 1):
            out.append(f"{u} {tag_of_u[u]} {pair_u[u]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        print("NO")

if __name__ == '__main__':
    solve()