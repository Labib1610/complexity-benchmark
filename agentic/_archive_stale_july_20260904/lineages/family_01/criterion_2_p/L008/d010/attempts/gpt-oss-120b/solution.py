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

    state = [0] * (n + 1)          # final answer, 0 = unassigned, 1 or 2
    parity = [-1] * (n + 1)       # temporary 0/1 inside current component
    q = deque()

    for start in range(1, n + 1):
        if state[start]:
            continue
        # new component, start BFS with parity 0
        parity[start] = 0
        q.append(start)
        component_vertices = [start]

        while q:
            u = q.popleft()
            pu = parity[u]
            for v in adj[u]:
                if parity[v] == -1:
                    parity[v] = 1 - pu
                    q.append(v)
                    component_vertices.append(v)
                elif parity[v] == pu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

        # assign final states: parity 0 -> 1, parity 1 -> 2
        for v in component_vertices:
            state[v] = 1 if parity[v] == 0 else 2
            parity[v] = -1          # reset for next component

    # all good
    out = ["YES\n"]
    out.append(' '.join(str(state[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()