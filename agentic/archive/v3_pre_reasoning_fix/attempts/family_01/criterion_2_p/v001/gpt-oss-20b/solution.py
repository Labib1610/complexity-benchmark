import sys
from collections import deque

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

    color = [-1] * (n + 1)
    team = [0] * (n + 1)
    comp_id = [-1] * (n + 1)
    comps = []

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp = [start]
        comp_id[start] = len(comps)
        bip = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    comp_id[v] = len(comps)
                    comp.append(v)
                    q.append(v)
                elif color[v] == color[u]:
                    bip = False
                    break
            if not bip:
                break
        if not bip:
            print("NO")
            return
        comps.append(comp)

    for comp in comps:
        minv = min(comp)
        orientation = 0 if color[minv] == 0 else 1
        for v in comp:
            team[v] = (color[v] ^ orientation) + 1

    print("YES")
    print(' '.join(map(str, team[1:])))

if __name__ == "__main__":
    solve()