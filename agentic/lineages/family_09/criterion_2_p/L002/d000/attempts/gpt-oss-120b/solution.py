import sys
import collections

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # 1) bipartition by BFS colouring
    color = [-1] * (n + 1)          # 0 = left, 1 = right
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = collections.deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)

    # 2) Hopcroft‑Karp
    pair = [0] * (n + 1)            # matched partner, 0 = free
    dist = [0] * (n + 1)

    def bfs() -> bool:
        dq = collections.deque()
        for u in range(1, n + 1):
            if color[u] == 0:               # left side only
                if pair[u] == 0:
                    dist[u] = 0
                    dq.append(u)
                else:
                    dist[u] = -1
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pair[v]
                if pu != 0 and dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                elif pu == 0:
                    found = True
        return found

    def dfs(u: int) -> bool:
        for v in adj[u]:
            pu = pair[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair[u] = v
                pair[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if color[u] == 0 and pair[u] == 0:
                if dfs(u):
                    matching += 1

    # 3) build a maximum independent set from the matching
    # alternating graph search
    left_vis = [False] * (n + 1)
    right_vis = [False] * (n + 1)
    dq = collections.deque()
    for u in range(1, n + 1):
        if color[u] == 0 and pair[u] == 0:   # free left vertices
            left_vis[u] = True
            dq.append(u)

    while dq:
        u = dq.popleft()
        if color[u] == 0:          # left → right via NON‑matched edges
            for v in adj[u]:
                if pair[u] != v and not right_vis[v]:
                    right_vis[v] = True
                    dq.append(v)
        else:                      # right → left via MATCHED edge only
            pu = pair[u]
            if pu != 0 and not left_vis[pu]:
                left_vis[pu] = True
                dq.append(pu)

    independent = []
    for v in range(1, n + 1):
        if color[v] == 0:
            if left_vis[v]:
                independent.append(v)
        else:
            if not right_vis[v]:
                independent.append(v)

    if len(independent) < k:
        sys.stdout.write("NO\n")
        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, independent[:k])) + "\n")


if __name__ == "__main__":
    solve()