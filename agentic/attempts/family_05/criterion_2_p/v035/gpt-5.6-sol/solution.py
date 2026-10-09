import sys
from collections import deque

def main():
    input_line = sys.stdin.buffer.readline
    k, t = map(int, input_line().split())

    adj = [[] for _ in range(k)]
    machine = [-1] * k

    for _ in range(t):
        x, y, z = map(int, input_line().split())
        x -= 1
        adj[x].append(z - 1)
        machine[x] = y

    if any(machine[x] == -1 for x in range(k)):
        print("NO")
        return

    pair_u = [-1] * k
    pair_v = [-1] * k
    dist = [0] * k
    ptr = [0] * k
    inf = k + 1

    sys.setrecursionlimit(5000)

    def bfs():
        queue = deque()
        shortest = inf

        for u in range(k):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = inf

        while queue:
            u = queue.popleft()
            if dist[u] >= shortest:
                continue

            next_dist = dist[u] + 1
            for v in adj[u]:
                matched_u = pair_v[v]
                if matched_u == -1:
                    shortest = next_dist
                elif dist[matched_u] == inf:
                    dist[matched_u] = next_dist
                    queue.append(matched_u)

        return shortest

    def dfs(u, shortest):
        edges = adj[u]
        while ptr[u] < len(edges):
            v = edges[ptr[u]]
            ptr[u] += 1
            matched_u = pair_v[v]

            if matched_u == -1:
                if dist[u] + 1 != shortest:
                    continue
            elif dist[matched_u] != dist[u] + 1 or not dfs(matched_u, shortest):
                continue

            pair_u[u] = v
            pair_v[v] = u
            return True

        dist[u] = inf
        return False

    matching = 0

    while True:
        shortest = bfs()
        if shortest == inf:
            break

        ptr[:] = [0] * k
        for u in range(k):
            if pair_u[u] == -1 and dfs(u, shortest):
                matching += 1

    if matching != k:
        print("NO")
        return

    output = ["YES"]
    for x in range(k):
        output.append(f"{x + 1} {machine[x]} {pair_u[x] + 1}")

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()