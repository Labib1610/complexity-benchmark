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

    colour = [-1] * (n + 1)          # 0 / 1 inside a component
    answer = [0] * (n + 1)           # final 1 / 2

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue

        # BFS of this component
        q = deque([start])
        colour[start] = 0
        comp = []                     # vertices of this component
        while q:
            v = q.popleft()
            comp.append(v)
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                elif colour[to] == cv:
                    sys.stdout.write("NO")
                    return

        # orient so that the smallest vertex (== start) gets role 1
        if colour[start] == 0:
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 1 if colour[v] == 1 else 2

    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()