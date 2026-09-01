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

    color = [ -1 ] * (n + 1)          # 0/1 bipartite color, -1 unvisited
    answer = [0] * (n + 1)            # final channel (1 or 2)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        part = [[], []]                # nodes with bipartite color 0 / 1
        part[0].append(start)
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    part[color[v]].append(v)
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print("NO")
            return

        # decide which side gets channel 1 (the smaller lexicographic)
        # the side containing the smallest node id gets 1
        min0 = min(part[0]) if part[0] else n+1
        min1 = min(part[1]) if part[1] else n+1
        if min0 < min1:
            for v in part[0]:
                answer[v] = 1
            for v in part[1]:
                answer[v] = 2
        else:
            for v in part[1]:
                answer[v] = 1
            for v in part[0]:
                answer[v] = 2

    # all components processed
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()