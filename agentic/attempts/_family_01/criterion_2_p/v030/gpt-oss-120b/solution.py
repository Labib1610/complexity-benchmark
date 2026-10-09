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

    color = [0] * (n + 1)          # 0 = unvisited, 1 or 2 = branch
    parity = [0] * (n + 1)         # temporary parity inside component (0/1)

    for start in range(1, n + 1):
        if color[start]:
            continue
        # start a new component, start will be the smallest index in it
        q = deque([start])
        parity[start] = 0
        comp_nodes = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not parity[v] and v != start and color[v]==0 and parity[v]==0 and v not in comp_nodes:
                    # not visited in this component
                    pass
                if parity[v] == 0 and color[v] == 0 and v not in comp_nodes:
                    # first time discovered in this component
                    parity[v] = parity[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif parity[v] != 0 or (v in comp_nodes):
                    # already discovered in this component
                    if parity[v] != parity[u] ^ 1:
                        ok = False
                        break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # assign colors: parity 0 -> 1, parity 1 -> 2 (so start gets 1)
        for node in comp_nodes:
            color[node] = 1 if parity[node] == 0 else 2

    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()