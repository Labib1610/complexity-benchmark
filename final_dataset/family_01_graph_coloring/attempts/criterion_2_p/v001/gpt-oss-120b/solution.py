import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = temporary colours

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start new component, start is its smallest vertex
        dq = deque([start])
        colour[start] = 0
        while dq:
            u = dq.popleft()
            cu = colour[u]
            for w in adj[u]:
                cw = colour[w]
                if cw == -1:
                    colour[w] = cu ^ 1
                    dq.append(w)
                elif cw == cu:
                    sys.stdout.write("NO")
                    return

    # feasible, build schedule (1/2) from temporary colours
    schedule = [str(colour[i] + 1) for i in range(1, n + 1)]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(schedule))

if __name__ == "__main__":
    solve()