import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    color = [0] * (n + 1)          # final colors 1 or 2
    parity = [ -1 ] * (n + 1)      # 0/1 for bipartition, -1 = unvisited
    for start in range(1, n + 1):
        if parity[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        parity[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            pu = parity[u]
            for v in adj[u]:
                if parity[v] == -1:
                    parity[v] = pu ^ 1
                    q.append(v)
                    comp.append(v)
                elif parity[v] == pu:
                    print("NO")
                    return
        # decide orientation for lexicographically smallest schedule
        min_vertex = min(comp)
        p_min = parity[min_vertex]
        for v in comp:
            color[v] = 1 if parity[v] == p_min else 2

    # all vertices colored
    print("YES")
    sys.stdout.write(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()