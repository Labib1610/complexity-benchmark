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

    color = [0] * (n + 1)          # 0 = unvisited, 1/2 = partition side (not final schedule)
    schedule = [0] * (n + 1)       # final answer 1/2
    from collections import deque

    for start in range(1, n + 1):
        if color[start]:
            continue
        # BFS to check bipartite and collect component
        q = deque([start])
        color[start] = 1
        comp = [start]
        part = {1: [], 2: []}
        part[1].append(start)
        ok = True
        while q and ok:
            u = q.popleft()
            cu = color[u]
            for v in g[u]:
                if not color[v]:
                    color[v] = 3 - cu
                    part[color[v]].append(v)
                    comp.append(v)
                    q.append(v)
                elif color[v] == cu:
                    ok = False
                    break
        if not ok:
            print("NO")
            return

        # decide orientation for lexicographically smallest schedule
        # build two possible assignments for this component
        # option A: part[1] -> 1, part[2] -> 2
        # option B: part[1] -> 2, part[2] -> 1
        # compare sequences on sorted vertex indices
        comp_sorted = sorted(comp)
        # generate color lists
        optA = []
        optB = []
        for v in comp_sorted:
            if v in part[1]:
                optA.append(1); optB.append(2)
            else:
                optA.append(2); optB.append(1)
        # choose smaller lexicographically
        if optA <= optB:
            for v in part[1]:
                schedule[v] = 1
            for v in part[2]:
                schedule[v] = 2
        else:
            for v in part[1]:
                schedule[v] = 2
            for v in part[2]:
                schedule[v] = 1

    print("YES")
    print(' '.join(str(schedule[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()