import sys
from collections import deque

def main():
    sys.setrecursionlimit(10000)
    read = sys.stdin.buffer.readline

    k, t = map(int, read().split())
    if t < k:
        print("NO")
        return

    adj = [[] for _ in range(k)]
    machine = [-1] * k
    pair_u = [-1] * k
    pair_v = [-1] * k
    matched = 0

    for _ in range(t):
        x, y, z = map(int, read().split())
        x -= 1
        z -= 1
        machine[x] = y
        adj[x].append(z)

        if pair_u[x] == -1 and pair_v[z] == -1:
            pair_u[x] = z
            pair_v[z] = x
            matched += 1

    dist = [-1] * k
    inf = k + 1

    while matched < k:
        queue = deque()
        for u in range(k):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1

        shortest = inf

        while queue:
            u = queue.popleft()
            next_dist = dist[u] + 1
            if next_dist > shortest:
                continue

            for v in adj[u]:
                other = pair_v[v]
                if other == -1:
                    if next_dist < shortest:
                        shortest = next_dist
                elif next_dist < shortest and dist[other] == -1:
                    dist[other] = next_dist
                    queue.append(other)

        if shortest == inf:
            break

        edge_pos = [0] * k

        def dfs(u):
            edges = adj[u]
            while edge_pos[u] < len(edges):
                v = edges[edge_pos[u]]
                edge_pos[u] += 1
                other = pair_v[v]

                if other == -1:
                    if dist[u] + 1 != shortest:
                        continue
                elif dist[other] != dist[u] + 1 or not dfs(other):
                    continue

                pair_u[u] = v
                pair_v[v] = u
                return True

            dist[u] = -1
            return False

        augmented = 0
        for u in range(k):
            if pair_u[u] == -1 and dfs(u):
                augmented += 1

        if augmented == 0:
            break
        matched += augmented

    if matched != k:
        print("NO")
        return

    output = ["YES"]
    for x in range(k):
        output.append(f"{x + 1} {machine[x]} {pair_u[x] + 1}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()