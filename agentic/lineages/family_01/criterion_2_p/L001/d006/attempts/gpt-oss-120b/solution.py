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

    if m == 0:
        # any assignment works, smallest is all 1
        print("YES")
        print(" ".join(["1"] * n))
        return

    # 0 = unvisited, 1/2 = final resonance level
    res = [0] * (n + 1)
    # temporary parity during BFS: 0 or 1
    parity = [0] * (n + 1)

    for start in range(1, n + 1):
        if res[start]:
            continue
        # start new component
        q = deque([start])
        parity[start] = 0
        comp = [start]
        part = [[], []]          # vertices with parity 0 / 1
        part[0].append(start)
        ok = True
        while q and ok:
            v = q.popleft()
            for to in adj[v]:
                if not res[to] and parity[to] == 0 and to not in part[0] and to not in part[1]:
                    # not visited yet in this component
                    parity[to] = parity[v] ^ 1
                    part[parity[to]].append(to)
                    comp.append(to)
                    q.append(to)
                else:
                    # already visited in this component
                    if parity[to] == parity[v]:
                        ok = False
                        break
        if not ok:
            print("NO")
            return
        # decide which parity gets resonance 1
        min_vertex = min(comp)
        if min_vertex in part[0]:
            one, two = 0, 1
        else:
            one, two = 1, 0
        for v in part[one]:
            res[v] = 1
        for v in part[two]:
            res[v] = 2

    # all vertices assigned
    print("YES")
    print(" ".join(str(res[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()