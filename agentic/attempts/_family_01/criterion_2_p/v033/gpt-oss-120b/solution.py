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

    color = [-1] * (n + 1)          # 0/1 bipartite colors
    answer = [0] * (n + 1)          # final shifts 1/2
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp_vertices = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp_vertices.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
        # decide orientation: smallest vertex gets shift 1
        min_v = min(comp_vertices)
        if color[min_v] == 0:
            # map 0->1, 1->2
            for v in comp_vertices:
                answer[v] = 1 if color[v] == 0 else 2
        else:
            # flip
            for v in comp_vertices:
                answer[v] = 1 if color[v] == 1 else 2

    print("YES")
    sys.stdout.write(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()