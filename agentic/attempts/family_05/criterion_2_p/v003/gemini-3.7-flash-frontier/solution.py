import sys

# Increase recursion depth for DFS in Hopcroft-Karp
sys.setrecursionlimit(200000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    adj = [[] for _ in range(k + 1)]
    machine = [0] * (k + 1)

    idx = 2
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        z = int(input_data[idx + 2])
        idx += 3
        adj[x].append(z)
        machine[x] = y

    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    dist = [0] * (k + 1)
    inf = float("inf")

    # Simple queue array for fast BFS
    queue = [0] * (k + 2)

    def bfs():
        head = 0
        tail = 0
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue[tail] = u
                tail += 1
            else:
                dist[u] = inf
        dist[0] = inf

        while head < tail:
            u = queue[head]
            head += 1
            if dist[u] < dist[0]:
                for v in adj[u]:
                    pv = pair_v[v]
                    if dist[pv] == inf:
                        dist[pv] = dist[u] + 1
                        queue[tail] = pv
                        tail += 1
        return dist[0] != inf

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                pv = pair_v[v]
                if dist[pv] == dist[u] + 1:
                    if dfs(pv):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = inf
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    if matching == k:
        out = ["YES"]
        for u in range(1, k + 1):
            out.append(f"{u} {machine[u]} {pair_u[u]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()