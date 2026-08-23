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

    color = [-1] * (n + 1)
    shift = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        min_node = start
        while q:
            u = q.popleft()
            if u < min_node:
                min_node = u
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    q.append(w)
                    comp_nodes.append(w)
                elif color[w] == color[u]:
                    sys.stdout.write("NO")
                    return

        # decide orientation based on color of the minimal node
        if color[min_node] == 0:
            for v in comp_nodes:
                shift[v] = 1 if color[v] == 0 else 2
        else:
            for v in comp_nodes:
                shift[v] = 1 if color[v] == 1 else 2

    out = ['YES', '\n', ' '.join(str(shift[i]) for i in range(1, n + 1))]
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()