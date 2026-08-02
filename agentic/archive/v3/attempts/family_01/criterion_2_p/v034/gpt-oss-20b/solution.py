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
    comps = []
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while q and ok:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    comp_nodes.append(v)
                    q.append(v)
                elif color[v] == cu:
                    ok = False
                    break
        if not ok:
            print("NO")
            return
        comps.append(comp_nodes)

    # Determine lexicographically smallest orientation
    comp_min = []
    for idx, comp in enumerate(comps):
        comp_min.append((min(comp), idx))
    comp_min.sort()

    res = [0] * (n + 1)
    for _, idx in comp_min:
        comp = comps[idx]
        # find minimal node and its color
        min_node = min(comp)
        min_color = color[min_node]
        if min_color == 0:
            # map 0->1,1->2
            for v in comp:
                res[v] = 1 if color[v] == 0 else 2
        else:
            # map 1->1,0->2
            for v in comp:
                res[v] = 1 if color[v] == 1 else 2

    print("YES")
    print(' '.join(str(res[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()