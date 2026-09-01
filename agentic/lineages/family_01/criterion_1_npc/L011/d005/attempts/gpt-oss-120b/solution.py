import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u].add(v)
        adj[v].add(u)

    # domain masks: bit 0 -> colour 1, bit1 -> colour2, bit2 -> colour3
    full_mask = 0b111
    dom0 = [full_mask] * n
    col0 = [0] * n                     # 0 = not fixed yet

    # ------------------------------------------------------------
    def propagate(col, dom, start_v, start_c):
        """apply colour start_c to start_v and propagate forced assignments.
           returns (True, col, dom) if no conflict, else (False, None, None)"""
        queue = [(start_v, start_c)]
        while queue:
            v, c = queue.pop()
            # already coloured ?
            if col[v] != 0:
                if col[v] != c:
                    return False, None, None
                continue
            col[v] = c
            mask_without_c = dom[v] & ~(1 << (c - 1))
            dom[v] = 1 << (c - 1)          # keep only the chosen colour
            for nb in adj[v]:
                if col[nb] != 0:
                    if col[nb] == c:
                        return False, None, None
                    continue
                if dom[nb] & (1 << (c - 1)):
                    dom[nb] &= ~(1 << (c - 1))
                    if dom[nb] == 0:
                        return False, None, None
                    # singleton domain -> forced colour
                    if dom[nb] & (dom[nb] - 1) == 0:   # power of two
                        forced_c = dom[nb].bit_length()   # 1..3
                        queue.append((nb, forced_c))
        return True, col, dom

    # ------------------------------------------------------------
    def dfs(idx, col, dom):
        # skip already coloured vertices
        while idx < n and col[idx] != 0:
            idx += 1
        if idx == n:
            return True

        allowed = dom[idx]
        for c in (1, 2, 3):
            if not (allowed & (1 << (c - 1))):
                continue
            # copy current state
            new_col = col[:]
            new_dom = dom[:]
            ok, new_col, new_dom = propagate(new_col, new_dom, idx, c)
            if not ok:
                continue
            if dfs(idx + 1, new_col, new_dom):
                # copy solution back to the outer arrays
                col[:] = new_col
                return True
        return False

    # ------------------------------------------------------------
    success = dfs(0, col0[:], dom0[:])
    out = sys.stdout
    if not success:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(" ".join(str(c) for c in col0) + "\n")

if __name__ == "__main__":
    solve()