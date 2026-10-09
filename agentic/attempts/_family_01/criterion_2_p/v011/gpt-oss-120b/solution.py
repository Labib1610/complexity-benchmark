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

    colour = [-1] * (n + 1)          # temporary 0/1 colours
    answer = [0] * (n + 1)           # final 1/2 bus numbers

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        colour[start] = 0
        comp = []                     # vertices of this component
        while q:
            v = q.popleft()
            comp.append(v)
            cv = colour[v]
            for nb in adj[v]:
                if colour[nb] == -1:
                    colour[nb] = cv ^ 1
                    q.append(nb)
                elif colour[nb] == cv:
                    sys.stdout.write("NO")
                    return

        # decide orientation: smallest index must become colour 0 (=> bus 1)
        min_v = min(comp)
        if colour[min_v] == 1:        # would become bus 2, so flip whole component
            for v in comp:
                colour[v] ^= 1

        for v in comp:
            answer[v] = colour[v] + 1   # map 0->1, 1->2

    out = ["YES\n"]
    out.append(' '.join(str(answer[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()