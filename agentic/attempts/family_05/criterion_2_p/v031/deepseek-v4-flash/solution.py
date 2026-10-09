import sys
from collections import deque

def hopcroft_karp(graph, n_left, n_right):
    INF = 10**9
    pair_u = [-1] * (n_left + 1)
    pair_v = [-1] * (n_right + 1)
    dist = [0] * (n_left + 1)

    def bfs():
        q = deque()
        for u in range(1, n_left + 1):
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
        for u in range(1, n_left + 1):
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

    # agent -> alias mapping
    agent_alias = [0] * (k + 1)
    # graph: agent -> list of frequencies
    graph = [[] for _ in range(k + 1)]

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        agent_alias[x] = y
        graph[x].append(z)

    # Check that aliases are distinct (given in problem, but safe)
    alias_set = set()
    for x in range(1, k + 1):
        if agent_alias[x] == 0:
            print("NO")
            return
        if agent_alias[x] in alias_set:
            print("NO")
            return
        alias_set.add(agent_alias[x])

    matching_size, pair_u = hopcroft_karp(graph, k, k)

    if matching_size != k:
        print("NO")
        return

    print("YES")
    for x in range(1, k + 1):
        z = pair_u[x]
        print(x, agent_alias[x], z)

if __name__ == "__main__":
    main()