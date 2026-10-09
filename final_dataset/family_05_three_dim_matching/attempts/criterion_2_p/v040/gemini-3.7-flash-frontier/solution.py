from collections import deque
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    station_of_drone = [-1] * k
    adj = [[] for _ in range(k)]

    idx = 2
    for _ in range(t):
        d = int(input_data[idx]) - 1
        c = int(input_data[idx + 1]) - 1
        f = int(input_data[idx + 2]) - 1
        idx += 3
        station_of_drone[d] = c
        adj[d].append(f)

    # Hopcroft-Karp algorithm
    pair_u = [-1] * k
    pair_v = [-1] * k
    dist = [-1] * k

    def bfs():
        queue = deque()
        for u in range(k):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1

        res = False
        while queue:
            u = queue.popleft()
            d_u = dist[u]
            for v in adj[u]:
                next_u = pair_v[v]
                if next_u == -1:
                    res = True
                elif dist[next_u] == -1:
                    dist[next_u] = d_u + 1
                    queue.append(next_u)
        return res

    def dfs(u):
        for v in adj[u]:
            next_u = pair_v[v]
            if next_u == -1 or (dist[next_u] == dist[u] + 1 and dfs(next_u)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(k):
            if pair_u[u] == -1:
                if dfs(u):
                    matching += 1

    if matching == k:
        out = ["YES"]
        for u in range(k):
            out.append(f"{u + 1} {station_of_drone[u] + 1} {pair_u[u] + 1}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()