import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    color = [ -1 ] * (n + 1)          # partition 0/1
    ans = [0] * (n + 1)               # final spin 1/2
    from collections import deque

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
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_vertices.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation: smallest index gets spin 1
        min_vertex = min(comp_vertices)
        part_of_min = color[min_vertex]
        # if part_of_min == 0 -> part0 ->1, else part0 ->2
        for v in comp_vertices:
            if color[v] == part_of_min:
                ans[v] = 1
            else:
                ans[v] = 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()