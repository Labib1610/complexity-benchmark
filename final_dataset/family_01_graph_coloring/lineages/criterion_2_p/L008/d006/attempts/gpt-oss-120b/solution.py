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
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n          # 0 = unvisited, 1 or 2 later
    parity = [-1] * n        # 0/1 bipartite side
    for i in range(n):
        if parity[i] != -1:
            continue
        # start new component
        q = deque([i])
        parity[i] = 0
        comp = [i]
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
        # decide which parity gets color 1 -> make smallest index vertex color 1
        min_vertex = min(comp)
        side_one = parity[min_vertex]   # this side will be color 1
        for v in comp:
            color[v] = 1 if parity[v] == side_one else 2

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()