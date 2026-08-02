import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        graph[u].append(v)
        graph[v].append(u)

    side = [-1] * (n + 1)       # 0 or 1
    ans = [0] * (n + 1)

    for s in range(1, n + 1):
        if side[s] != -1:
            continue

        # new component
        side[s] = 0
        q = deque([s])
        comp = [s]
        min_v = s

        while q:
            u = q.popleft()
            for v in graph[u]:
                if side[v] == -1:
                    side[v] = 1 - side[u]
                    q.append(v)
                    comp.append(v)
                    if v < min_v:
                        min_v = v
                else:
                    if side[v] == side[u]:
                        sys.stdout.write("NO\n")
                        return

        # colouring that gives colour 1 to the smallest vertex
        if side[min_v] == 0:
            for x in comp:
                ans[x] = side[x] + 1      # 0->1 , 1->2
        else:
            for x in comp:
                ans[x] = 2 - side[x]      # 1->1 , 0->2

    out_lines = ["YES"] + [str(ans[i]) for i in range(1, n + 1)]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()