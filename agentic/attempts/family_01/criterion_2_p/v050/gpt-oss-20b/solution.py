import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n          # 0 or 1
    final = [0] * n           # final 0/1 before +1
    visited = [False] * n

    for start in range(n):
        if visited[start]:
            continue
        # BFS to explore component
        queue = deque([start])
        visited[start] = True
        color[start] = 0
        comp_vertices = [start]
        ok = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = color[u] ^ 1
                    queue.append(v)
                    comp_vertices.append(v)
                else:
                    if color[v] == color[u]:
                        ok = False
                        break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # decide lexicographically minimal coloring for this component
        comp_vertices.sort()
        seq0 = [color[v] for v in comp_vertices]
        seq1 = [1 - c for c in seq0]
        if tuple(seq0) <= tuple(seq1):
            chosen = seq0
            for idx, v in enumerate(comp_vertices):
                final[v] = chosen[idx]
        else:
            chosen = seq1
            for idx, v in enumerate(comp_vertices):
                final[v] = chosen[idx]

    # Output
    out = ['YES', '\n']
    out.append(' '.join(str(c + 1) for c in final))
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()