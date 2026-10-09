import sys
sys.setrecursionlimit(10000)

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

    col = [0] * (n + 1)          # 0 = uncoloured
    forbid = [0] * (n + 1)       # bitmask, bit 0 -> colour 1, etc.

    BIT = [1, 2, 4]              # 1<<0,1<<1,1<<2

    def dfs(v: int) -> bool:
        if v == n + 1:
            return True
        mask = forbid[v]
        for c in range(3):      # c = 0,1,2 corresponds to colour c+1
            if not (mask & BIT[c]):
                col[v] = c + 1
                changed = []
                bit = BIT[c]
                for nb in adj[v]:
                    if col[nb] == 0 and not (forbid[nb] & bit):
                        forbid[nb] |= bit
                        changed.append(nb)
                if dfs(v + 1):
                    return True
                # undo
                for nb in changed:
                    forbid[nb] &= ~bit
                col[v] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(col[i]) for i in range(1, n + 1))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()