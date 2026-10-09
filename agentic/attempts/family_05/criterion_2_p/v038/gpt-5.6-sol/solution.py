import sys
from collections import deque

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adjacency = [[] for _ in range(k + 1)]
    relay = [0] * (k + 1)

    for _ in range(t):
        u, v, w = map(int, input_buffer.readline().split())
        adjacency[u].append(w)
        relay[u] = v

    if any(not adjacency[u] for u in range(1, k + 1)):
        print("NO")
        return

    pair_u = [0] * (k + 1)
    pair_w = [0] * (k + 1)
    dist = [0] * (k + 1)
    ptr = [0] * (k + 1)
    inf = k + 1

    sys.setrecursionlimit(1000000)

    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = inf

        dist[0] = inf

        while queue:
            u = queue.popleft()
            if dist[u] >= dist[0]:
                continue
            for w in adjacency[u]:
                next_u = pair_w[w]
                if dist[next_u] == inf:
                    dist[next_u] = dist[u] + 1
                    if next_u != 0:
                        queue.append(next_u)

        return dist[0] != inf

    def dfs(u):
        while ptr[u] < len(adjacency[u]):
            w = adjacency[u][ptr[u]]
            ptr[u] += 1
            next_u = pair_w[w]

            if dist[next_u] == dist[u] + 1 and (next_u == 0 or dfs(next_u)):
                pair_u[u] = w
                pair_w[w] = u
                return True

        dist[u] = inf
        return False

    matching = 0
    while bfs():
        ptr[1:] = [0] * k
        for u in range(1, k + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    output = ["YES"]
    for u in range(1, k + 1):
        output.append(f"{u} {relay[u]} {pair_u[u]}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()