import sys
sys.setrecursionlimit(1 << 25)

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

    color = [ -1 ] * (n + 1)          # 0 / 1 bipartite colors
    answer = [0] * (n + 1)

    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        min_vertex = start
        while q:
            u = q.popleft()
            if u < min_vertex:
                min_vertex = u
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
        # decide orientation: min_vertex must get shift 1
        base_color = color[min_vertex]
        for v in comp:
            answer[v] = 1 if color[v] == base_color else 2

    # all vertices processed
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()