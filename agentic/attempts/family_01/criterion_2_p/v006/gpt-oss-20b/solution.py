import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # -1 unvisited, 0/1 colors
    ans = [0] * (n + 1)             # final 1/2 assignment

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp = [start]
        bip = True
        while q and bip:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    bip = False
                    break
        if not bip:
            print("NO")
            return

        min_node = min(comp)
        min_color = color[min_node]
        # mapping: color -> line number
        if min_color == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for node in comp:
            ans[node] = map0 if color[node] == 0 else map1

    print("YES")
    print(' '.join(map(str, ans[1:])))

if __name__ == "__main__":
    solve()