import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        bit_u = 1 << u
        bit_v = 1 << v
        if not (adj[u] & bit_v):
            adj[u] |= bit_v
            adj[v] |= bit_u
            adj_list[u].append(v)
            adj_list[v].append(u)

    ALL = (1 << n) - 1
    degs = [len(adj_list[v]) for v in range(n)]

    def is_colorable(fixed):
        color_masks = [0, 0, 0, 0]
        colored = 0
        for v in range(n):
            c = fixed[v]
            if c:
                bit = 1 << v
                if adj[v] & color_masks[c]:
                    return False
                color_masks[c] |= bit
                colored |= bit

        forbid = [0, 0, 0, 0]
        for v in range(n):
            c = fixed[v]
            if c:
                forbid[c] |= adj[v]

        if (forbid[1] & forbid[2] & forbid[3]) & (ALL ^ colored):
            return False

        uncolored = n - colored.bit_count()

        def dfs():
            nonlocal colored, uncolored
            if uncolored == 0:
                return True

            best_v = -1
            best_avail = 4
            best_deg = -1
            rem = ALL ^ colored
            mm = rem
            while mm:
                lsb = mm & -mm
                v = lsb.bit_length() - 1
                avail = 3 - ((forbid[1] >> v & 1) +
                             (forbid[2] >> v & 1) +
                             (forbid[3] >> v & 1))
                if avail == 0:
                    return False
                d = degs[v]
                if avail < best_avail or (avail == best_avail and d > best_deg):
                    best_v = v
                    best_avail = avail
                    best_deg = d
                mm ^= lsb

            v = best_v
            bit = 1 << v
            for c in (1, 2, 3):
                if forbid[c] & bit:
                    continue
                colored |= bit
                uncolored -= 1
                old = forbid[c]
                forbid[c] |= adj[v]
                if not ((forbid[1] & forbid[2] & forbid[3]) & (ALL ^ colored)):
                    if dfs():
                        return True
                forbid[c] = old
                colored ^= bit
                uncolored += 1
            return False

        return dfs()

    if not is_colorable([0] * n):
        sys.stdout.write("NO")
        return

    ans = [0] * n
    for i in range(n):
        local_forbid = 0
        for u in adj_list[i]:
            if ans[u]:
                local_forbid |= 1 << ans[u]
        chosen = False
        for c in (1, 2, 3):
            if local_forbid & (1 << c):
                continue
            ans[i] = c
            if is_colorable(ans):
                chosen = True
                break
            ans[i] = 0
        if not chosen:
            sys.stdout.write("NO")
            return

    out = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()