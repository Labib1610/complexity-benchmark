import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    side = [0] * (n + 1)          # temporary bipartition 0/1
    answer = [0] * (n + 1)

    from collections import deque

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS for this component
        q = deque([start])
        visited[start] = True
        side[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    side[v] = side[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif side[v] == side[u]:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

        # decide orientation: smallest vertex gets shift 1
        min_v = min(comp)
        side_one = side[min_v]          # side that will become shift 1
        for v in comp:
            answer[v] = 1 if side[v] == side_one else 2

    # all components processed, feasible
    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()