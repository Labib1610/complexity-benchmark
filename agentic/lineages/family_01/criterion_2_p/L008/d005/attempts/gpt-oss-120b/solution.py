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

    # special case: no edges -> all 1s
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return

    color = [ -1 ] * (n + 1)          # parity 0/1, -1 = unvisited
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        minv = start
        ok = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    comp.append(to)
                    if to < minv:
                        minv = to
                elif color[to] == color[v]:
                    # odd cycle
                    print("NO")
                    return
        # decide orientation
        if color[minv] == 0:
            # 0 -> 1, 1 -> 2
            for v in comp:
                answer[v] = 1 if color[v] == 0 else 2
        else:
            # swap
            for v in comp:
                answer[v] = 2 if color[v] == 0 else 1

    # output
    print("YES")
    print(" ".join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()