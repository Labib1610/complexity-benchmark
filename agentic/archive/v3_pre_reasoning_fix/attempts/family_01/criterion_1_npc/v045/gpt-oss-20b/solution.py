import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data: 
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0]*n
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        if u==v: continue
        adj[u] |= 1<<v
        adj[v] |= 1<<u

    colors = [0]*n          # 0 unassigned, 1/2/3 assigned
    color_mask = [0,0,0,0]   # index by color; bitmask of nodes with that color

    solution = None

    def forward_check(idx):
        # check all unassigned nodes j > idx
        for j in range(idx+1, n):
            if colors[j]!=0: continue
            allowed = 0
            # color 1
            if (adj[j] & color_mask[1]) == 0:
                allowed |= 1
            # color 2
            if (adj[j] & color_mask[2]) == 0:
                allowed |= 2
            # color 3
            if (adj[j] & color_mask[3]) == 0:
                allowed |= 4
            if allowed == 0:
                return False
        return True

    def dfs(idx):
        nonlocal solution
        if solution is not None:
            return
        if idx == n:
            solution = colors[:]
            return
        for c in (1,2,3):
            if (adj[idx] & color_mask[c]) == 0:
                colors[idx] = c
                color_mask[c] |= 1<<idx
                if forward_check(idx):
                    dfs(idx+1)
                colors[idx] = 0
                color_mask[c] &= ~(1<<idx)
                if solution is not None:
                    return

    dfs(0)
    out = []
    if solution is None:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(x) for x in solution))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()