import sys
sys.setrecursionlimit(1 << 25)

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

    colour = [-1] * (n + 1)          # 0 / 1
    answer = [0] * (n + 1)
    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp_vertices = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)
                    comp_vertices.append(v)
                elif colour[v] == cu:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print("NO")
            return

        # decide orientation: make start (the smallest vertex) have value 1
        if colour[start] == 0:
            # colour 0 -> 1, colour 1 -> 2
            for v in comp_vertices:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            # colour 1 -> 1, colour 0 -> 2
            for v in comp_vertices:
                answer[v] = 1 if colour[v] == 1 else 2

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()