import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # vehicle assigned to each agent (unique per agent)
    agent_vehicle = [0] * (k + 1)
    # adjacency list from agent to sectors
    adj = [[] for _ in range(k + 1)]

    for _ in range(t):
        a = int(next(it))
        v = int(next(it))
        s = int(next(it))
        if agent_vehicle[a] == 0:
            agent_vehicle[a] = v
        # all entries for same agent have same vehicle, guaranteed
        adj[a].append(s)

    # quick check: every agent must have at least one possible sector
    for a in range(1, k + 1):
        if not adj[a]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)          # agent -> sector
    pair_v = [0] * (k + 1)          # sector -> agent (sectors are 1..k)
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in adj[u]:
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    print("YES")
    out_lines = []
    for a in range(1, k + 1):
        v = agent_vehicle[a]
        s = pair_u[a]
        out_lines.append(f"{a} {v} {s}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()