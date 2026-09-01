import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    provisional = [-1] * n          # 0 / 1 provisional colours
    answer = [0] * n                # final windows (1 or 2)

    for start in range(n):
        if provisional[start] != -1:
            continue

        # BFS of this component
        q = deque([start])
        provisional[start] = 0
        comp = [start]
        bipartite = True

        while q and bipartite:
            u = q.popleft()
            cu = provisional[u]
            for v in g[u]:
                cv = provisional[v]
                if cv == -1:
                    provisional[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif cv == cu:
                    bipartite = False
                    break

        if not bipartite:
            print("NO")
            return

        # orient component so that its smallest index gets window 1
        min_vertex = min(comp)
        if provisional[min_vertex] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1

        for v in comp:
            answer[v] = map0 if provisional[v] == 0 else map1

    print("YES")
    sys.stdout.write(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()