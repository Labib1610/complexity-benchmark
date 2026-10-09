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

    colour = [-1] * (n + 1)          # -1 unvisited, 0 -> mode 1, 1 -> mode 2
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == cv:
                    print("NO")
                    return
        # decide orientation for lexicographic minimality
        v_min = min(comp)
        if colour[v_min] == 1:          # need to flip
            for x in comp:
                colour[x] ^= 1

    # build answer
    ans = ['1' if colour[i] == 0 else '2' for i in range(1, n + 1)]
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()