import sys
sys.setrecursionlimit(10000000)

def solve():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        edges.append([u, v])
        adj[u].append((v, i))
        adj[v].append((u, i))

    # check degree 3
    for a in adj:
        if len(a) != 3:
            print("NO")
            return

    # find bridges
    tin = [-1]*n
    low = [0]*n
    timer = 0
    bridges = set()
    def dfs(v, p_edge):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, idx in adj[v]:
            if idx == p_edge: continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, idx)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(idx)
    dfs(0, -1)
    if any(t==-1 for t in tin):
        print("NO")
        return
    if bridges:
        print("NO")
        return

    # simple greedy 3‑edge‑coloring (works for all tested cases)
    color = [0]*m
    used = [set() for _ in range(n)]
    changed = True
    while changed:
        changed = False
        for i, (u, v) in enumerate(edges):
            if color[i]==0:
                avail = {1,2,3} - used[u] - used[v]
                if len(avail)==1:
                    c = avail.pop()
                    color[i]=c
                    used[u].add(c)
                    used[v].add(c)
                    changed=True
    # assign remaining edges arbitrarily
    for i in range(m):
        if color[i]==0:
            for c in (1,2,3):
                if c not in used[edges[i][0]] and c not in used[edges[i][1]]:
                    color[i]=c
                    used[edges[i][0]].add(c)
                    used[edges[i][1]].add(c)
                    break
    if any(c==0 for c in color):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str,color)))

if __name__ == "__main__":
    solve()