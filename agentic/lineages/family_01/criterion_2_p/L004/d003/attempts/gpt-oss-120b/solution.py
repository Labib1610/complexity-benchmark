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

    colour = [-1] * (n + 1)          # 0 / 1 during BFS
    answer = [0] * (n + 1)           # final s_i (1 or 2)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == cv:
                    # not bipartite
                    print("NO")
                    return
        # decide orientation: make start vertex have value 1
        if colour[start] == 0:
            # 0 -> 1, 1 -> 2
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            # 1 -> 1, 0 -> 2
            for v in comp:
                answer[v] = 1 if colour[v] == 1 else 2

    # all done
    print("YES")
    sys.stdout.write(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()