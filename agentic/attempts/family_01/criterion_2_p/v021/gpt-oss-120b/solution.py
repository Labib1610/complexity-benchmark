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

    parity = [-1] * (n + 1)          # -1 = unvisited, else 0/1
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if parity[start] != -1:
            continue

        # new component, start is its smallest vertex
        q = deque([start])
        parity[start] = 0
        comp = [start]

        while q:
            u = q.popleft()
            pu = parity[u]
            for v in adj[u]:
                if parity[v] == -1:
                    parity[v] = pu ^ 1
                    q.append(v)
                    comp.append(v)
                elif parity[v] == pu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

        # assign numbers: parity 0 -> 1, parity 1 -> 2
        for v in comp:
            answer[v] = 1 if parity[v] == 0 else 2

    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()