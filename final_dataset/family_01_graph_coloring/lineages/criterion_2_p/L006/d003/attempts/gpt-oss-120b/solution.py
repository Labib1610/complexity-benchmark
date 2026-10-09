import sys
sys.setrecursionlimit(1 << 25)

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

    color = [0] * (n + 1)          # final answer 1/2, 0 = unassigned
    parity = [-1] * (n + 1)        # temporary 0/1 during BFS
    from collections import deque

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
        # decide orientation: smallest vertex gets colour 1
        vmin = min(comp)
        if parity[vmin] == 0:
            # parity 0 -> 1, parity 1 -> 2
            for v in comp:
                color[v] = 1 if parity[v] == 0 else 2
        else:
            # swap
            for v in comp:
                color[v] = 1 if parity[v] == 1 else 2

    # all vertices assigned
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()