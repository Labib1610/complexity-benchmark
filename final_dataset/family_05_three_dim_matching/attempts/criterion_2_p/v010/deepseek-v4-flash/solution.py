import sys
from collections import deque

def hopcroft_karp(graph, n_left, n_right):
    INF = 10**9
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = [0] * n_left

    def bfs():
        q = deque()
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in graph[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in graph[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # specialist -> machine mapping
    spec_machine = [0] * (k + 1)
    # availability: for each specialist, set of time slots
    avail = [[] for _ in range(k + 1)]

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        spec_machine[x] = y
        avail[x].append(z)

    # Build bipartite graph: left = specialists (0..k-1), right = time slots (0..k-1)
    graph = [[] for _ in range(k)]
    for spec in range(1, k + 1):
        for slot in avail[spec]:
            graph[spec - 1].append(slot - 1)

    matching_count, pair_u = hopcroft_karp(graph, k, k)

    if matching_count < k:
        print("NO")
    else:
        print("YES")
        for spec in range(1, k + 1):
            slot = pair_u[spec - 1] + 1
            machine = spec_machine[spec]
            print(spec, machine, slot)

if __name__ == "__main__":
    main()