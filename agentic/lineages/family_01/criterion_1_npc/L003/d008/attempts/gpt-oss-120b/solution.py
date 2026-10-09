import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n                     # bitmask of neighbours
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # 3-bit mask, bit 0 -> colour 1, bit 1 -> colour 2, bit 2 -> colour 3
    domain = [0b111] * n
    colour = [-1] * n                 # -1 = unassigned

    ALL = (1 << n) - 1                # all vertices still unassigned
    answer = None                     # will hold final colours (0‑based)

    # -------------------------------------------------------------
    def dfs(unassigned_mask: int) -> bool:
        nonlocal answer
        if unassigned_mask == 0:          # all coloured
            answer = colour[:]
            return True

        # ---- choose vertex with smallest domain (MRV) ----
        v = -1
        min_sz = 4
        mask = unassigned_mask
        while mask:
            lsb = mask & -mask
            i = (lsb.bit_length() - 1)
            sz = domain[i].bit_count()
            if sz < min_sz:
                min_sz = sz
                v = i
                if sz == 1:
                    break
            mask ^= lsb
        if min_sz == 0:            # dead end
            return False

        # ---- try every possible colour for v ----
        allowed = domain[v]
        for c in range(3):
            if not (allowed >> c) & 1:
                continue
            # assign colour c to v
            colour[v] = c
            new_unassigned = unassigned_mask & ~(1 << v)

            # forward checking: remove colour c from neighbours
            modified = []          # list of (vertex, old_domain)
            contradiction = False
            neigh = adj[v] & new_unassigned
            while neigh:
                lsb = neigh & -neigh
                u = (lsb.bit_length() - 1)
                if (domain[u] >> c) & 1:
                    old = domain[u]
                    new = old & ~(1 << c)
                    modified.append((u, old))
                    domain[u] = new
                    if new == 0:
                        contradiction = True
                        break
                neigh ^= lsb

            if not contradiction:
                if dfs(new_unassigned):
                    return True

            # ---- backtrack: restore domains ----
            for u, old in reversed(modified):
                domain[u] = old
            colour[v] = -1

        return False
    # -------------------------------------------------------------

    ok = dfs(ALL)

    out = sys.stdout
    if not ok:
        out.write("NO\n")
    else:
        out.write("YES\n")
        # convert 0‑based colours to 1‑based numbers
        out.write(" ".join(str(c + 1) for c in answer) + "\n")

if __name__ == "__main__":
    solve()