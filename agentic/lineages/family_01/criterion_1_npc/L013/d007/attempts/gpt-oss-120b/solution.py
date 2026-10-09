import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # precompute allowed pairs (a,b) where (a^3+b^3) % (a^2+b^2) != 0
    ok = [[True]*4 for _ in range(4)]  # 1-indexed
    for a in range(1,4):
        for b in range(1,4):
            phi = a**3 + b**3
            B = a**2 + b**2
            ok[a][b] = (phi % B != 0)

    # ordering vertices by degree descending for heuristic
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0]*n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colors = [0]*n
    used = [False]*n

    def dfs(k: int) -> bool:
        if k == n:
            return True
        v = order[k]
        # try colors 1..3
        for c in (1,2,3):
            good = True
            for nb in adj[v]:
                if colors[nb]:
                    if not ok[c][colors[nb]]:
                        good = False
                        break
            if good:
                colors[v] = c
                if dfs(k+1):
                    return True
                colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()