import sys
sys.setrecursionlimit(10000)

def det3(m):
    a,b,c = m[0]
    d,e,f = m[1]
    g,h,i = m[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

# precompute allowed pairs
allowed = [[False]*4 for _ in range(4)]  # 1..3
for su in (1,2,3):
    for sv in (1,2,3):
        M = [
            [1, su+2, su*su + 4*sv],
            [1, sv, sv*sv],
            [1, sv+1, sv*sv + 2*sv]
        ]
        allowed[su][sv] = det3(M) != 0

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        adj[u].append(v)
        adj[v].append(u)
    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0]*n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    # for quick check of already assigned neighbors
    assignment = [0]*n
    found = False

    def dfs(idx):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try colors 1..3 to get minimal V_n (lexicographically minimal in original order)
        for col in (1,2,3):
            ok = True
            for nb in adj[v]:
                if assignment[nb]:
                    if not allowed[col][assignment[nb]]:
                        ok = False
                        break
            if not ok:
                continue
            assignment[v] = col
            dfs(idx+1)
            if found:
                return
            assignment[v] = 0

    dfs(0)
    if not found:
        print("NO")
    else:
        # need output in original order 1..n, but also ensure minimal V_n.
        # Our search order may not guarantee minimal V_n globally because we colored by degree order.
        # To enforce minimal V_n, we can after finding any solution, perform a DFS that respects original order,
        # using the found solution as upper bound. Simpler: redo backtracking in original order with pruning using allowed matrix and stop at first solution.
        # Since n<=40, this is fine.
        assignment = [0]*n
        found = False
        def dfs2(i):
            nonlocal found
            if found:
                return
            if i==n:
                found=True
                return
            v = i  # original order
            for col in (1,2,3):
                ok=True
                for nb in adj[v]:
                    if nb< i and assignment[nb]:
                        if not allowed[col][assignment[nb]]:
                            ok=False
                            break
                if not ok:
                    continue
                assignment[v]=col
                dfs2(i+1)
                if found:
                    return
                assignment[v]=0
        dfs2(0)
        print("YES")
        print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()