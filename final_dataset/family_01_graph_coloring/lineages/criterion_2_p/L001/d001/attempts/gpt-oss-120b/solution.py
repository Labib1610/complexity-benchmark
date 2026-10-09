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

    color = [ -1 ] * (n + 1)          # 0 or 1 for bipartition, -1 unvisited
    ans = [0] * (n + 1)               # final tier values (1 or 2)

    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        part = [[], []]               # nodes of each side
        part[0].append(start)
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    part[color[v]].append(v)
                    q.append(v)
                elif color[v] == cu:
                    # not bipartite
                    print("NO")
                    return
        # decide orientation for lexicographically smallest assignment
        # find minimal index in each side (if side empty, set to large)
        min0 = min(part[0]) if part[0] else n + 1
        min1 = min(part[1]) if part[1] else n + 1
        if min0 < min1:
            # side 0 gets tier 1, side 1 gets tier 2
            for v in part[0]:
                ans[v] = 1
            for v in part[1]:
                ans[v] = 2
        else:
            # side 1 gets tier 1
            for v in part[1]:
                ans[v] = 1
            for v in part[0]:
                ans[v] = 2

    # all components processed successfully
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()