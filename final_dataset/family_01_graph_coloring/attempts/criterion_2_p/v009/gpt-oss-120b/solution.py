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

    color = [-1] * (n + 1)          # 0 or 1
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
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_vertices.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation: smallest index gets shift 1
        min_vertex = min(comp_vertices)
        min_color = color[min_vertex]
        # if min_color == 0 -> keep mapping 0->1,1->2; else flip
        if min_color == 0:
            for v in comp_vertices:
                answer[v] = 1 if color[v] == 0 else 2
        else:
            for v in comp_vertices:
                answer[v] = 1 if color[v] == 1 else 2

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()