import sys
from collections import deque

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

    color = [-1] * (n + 1)          # parity 0/1 for bipartition
    answer = [0] * (n + 1)          # final values 1/2
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return
        # decide which parity gets value 1
        min_node = min(comp)
        parity_of_min = color[min_node]
        # parity_of_min -> 1, other -> 2
        for v in comp:
            answer[v] = 1 if color[v] == parity_of_min else 2

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()