import sys

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

    # ---------- 1. forbidden table ----------
    forbidden = [[False] * 4 for _ in range(4)]  # 1..3 used
    for a in (1, 2, 3):
        for b in (1, 2, 3):
            if (a ** b + b ** a + a * b) % 3 == 0:
                forbidden[a][b] = True

    allowed = [[] for _ in range(4)]
    for a in (1, 2, 3):
        for b in (1, 2, 3):
            if not forbidden[a][b]:
                allowed[a].append(b)

    # ---------- 2. domains ----------
    ALL = 0b111  # bits 0,1,2 correspond to colours 1,2,3
    domain = [ALL] * n
    color = [0] * n  # 0 = unassigned, else 1..3

    # ---------- 3. helper ----------
    def bits_to_list(mask):
        res = []
        if mask & 1:
            res.append(1)
        if mask & 2:
            res.append(2)
        if mask & 4:
            res.append(3)
        return res

    sys.setrecursionlimit(10000)

    # ---------- 4. backtracking ----------
    def dfs(assigned_cnt: int) -> bool:
        if assigned_cnt == n:
            return True

        # MRV: choose vertex with smallest non‑zero domain
        v = -1
        best = 4
        for i in range(n):
            if color[i] == 0:
                sz = (domain[i] & 1) + ((domain[i] >> 1) & 1) + ((domain[i] >> 2) & 1)
                if sz < best:
                    best = sz
                    v = i
                    if sz == 1:
                        break
        if best == 0:          # empty domain -> dead end
            return False

        cur_mask = domain[v]
        for c in bits_to_list(cur_mask):
            # assign colour c to v
            color[v] = c
            saved = []          # (neighbor, old_mask)
            ok = True
            for nb in adj[v]:
                if color[nb] != 0:
                    # already coloured, just check compatibility
                    if forbidden[c][color[nb]]:
                        ok = False
                        break
                else:
                    # shrink neighbour's domain
                    old = domain[nb]
                    # keep only colours compatible with c
                    mask = 0
                    for d in allowed[c]:
                        mask |= 1 << (d - 1)
                    new = old & mask
                    if new != old:
                        saved.append((nb, old))
                        domain[nb] = new
                    if new == 0:
                        ok = False
                        break
            if ok and dfs(assigned_cnt + 1):
                return True
            # restore
            for nb, old in saved:
                domain[nb] = old
            color[v] = 0
        return False

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(color[i]) for i in range(n)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()