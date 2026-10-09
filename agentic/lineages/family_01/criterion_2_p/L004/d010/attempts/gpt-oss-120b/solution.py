import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().split()
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

    state = [0] * (n + 1)          # final answer: 1 or 2, 0 = unvisited
    color = [-1] * (n + 1)         # temporary 0/1 during BFS
    ok = True

    for start in range(1, n + 1):
        if state[start]:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break

        # choose orientation: smallest vertex gets state 1
        min_v = min(comp)
        if color[min_v] == 1:          # need to flip
            for v in comp:
                color[v] ^= 1
        for v in comp:
            state[v] = color[v] + 1     # 1 or 2

    out = sys.stdout
    if not ok:
        out.write("NO")
    else:
        out.write("YES\n")
        out.write(' '.join(str(state[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()