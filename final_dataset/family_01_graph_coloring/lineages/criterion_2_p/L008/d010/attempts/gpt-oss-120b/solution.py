import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    parity = [-1] * n          # -1 unvisited, else 0/1
    answer = [0] * n
    for start in range(n):
        if parity[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        parity[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if parity[to] == -1:
                    parity[to] = parity[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif parity[to] == parity[v]:
                    print("NO")
                    return
        # choose orientation to make smallest index get color 1
        first = min(comp)
        if parity[first] == 0:
            # parity 0 -> color 1, parity 1 -> color 2
            for v in comp:
                answer[v] = 1 if parity[v] == 0 else 2
        else:
            # parity 1 -> color 1
            for v in comp:
                answer[v] = 1 if parity[v] == 1 else 2

    # all components processed, graph is bipartite
    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()