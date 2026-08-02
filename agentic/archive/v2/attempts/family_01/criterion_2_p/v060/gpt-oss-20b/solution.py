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
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    parity = [-1] * (n + 1)  # -1 = unvisited, 0/1 = parity
    result = [0] * (n + 1)   # vault numbers (1 or 2)

    for start in range(1, n + 1):
        if parity[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        parity[start] = 0
        component = [start]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if parity[v] == -1:
                    parity[v] = parity[u] ^ 1
                    q.append(v)
                    component.append(v)
                elif parity[v] == parity[u]:
                    # Not bipartite
                    sys.stdout.write("NO")
                    return

        # lexicographically smallest: make the smallest index in component vault 1
        flip = parity[start]  # start is the smallest index in this component
        for v in component:
            vault = (parity[v] ^ flip) + 1  # 1 or 2
            result[v] = vault

    # All components processed successfully
    out_lines = ["YES", " ".join(str(result[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()