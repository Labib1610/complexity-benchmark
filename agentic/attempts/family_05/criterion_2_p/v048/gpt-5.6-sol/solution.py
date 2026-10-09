import sys
from collections import deque

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adj = [[] for _ in range(k)]
    column = [-1] * k
    pair_left = [-1] * k
    pair_right = [-1] * k
    matched = 0

    for _ in range(t):
        e, d, i = map(int, input_buffer.readline().split())
        e -= 1
        i -= 1
        adj[e].append(i)
        column[e] = d

        if pair_left[e] == -1 and pair_right[i] == -1:
            pair_left[e] = i
            pair_right[i] = e
            matched += 1

    if t < k or any(not edges for edges in adj):
        sys.stdout.write("NO\n")
        return

    sys.setrecursionlimit(5000)
    inf = k + 1
    dist = [inf] * k
    next_edge = [0] * k
    shortest = inf

    def bfs():
        nonlocal shortest
        queue = deque()
        for u in range(k):
            if pair_left[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = inf

        shortest = inf
        while queue:
            u = queue.popleft()
            if dist[u] >= shortest:
                continue

            next_dist = dist[u] + 1
            for v in adj[u]:
                other = pair_right[v]
                if other == -1:
                    shortest = next_dist
                elif dist[other] == inf:
                    dist[other] = next_dist
                    queue.append(other)

        return shortest != inf

    def dfs(u):
        edges = adj[u]
        index = next_edge[u]

        while index < len(edges):
            v = edges[index]
            next_edge[u] = index + 1
            other = pair_right[v]

            if other == -1:
                if dist[u] + 1 == shortest:
                    pair_left[u] = v
                    pair_right[v] = u
                    return True
            elif dist[other] == dist[u] + 1 and dfs(other):
                pair_left[u] = v
                pair_right[v] = u
                return True

            index = next_edge[u]

        dist[u] = inf
        return False

    while matched < k and bfs():
        next_edge = [0] * k
        for u in range(k):
            if pair_left[u] == -1 and dfs(u):
                matched += 1

    if matched != k:
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    output.extend(
        f"{u + 1} {column[u]} {pair_left[u] + 1}"
        for u in range(k)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()