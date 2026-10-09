import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n               # bitmask of neighbours
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # 3 bits: colour 1 -> bit 0, colour 2 -> bit 1, colour 3 -> bit 2
    allowed = [0b111] * n
    col = [0] * n               # 0 = not coloured yet

    # depth‑first search, vertices are processed in order 0 .. n-1
    def dfs(v: int) -> bool:
        if v == n:
            return True

        mask = allowed[v]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (mask & bit):
                continue

            # assign colour c to vertex v
            col[v] = c
            changed = []          # neighbours whose mask lost this bit
            conflict = False

            neigh = adj[v]
            while neigh:
                lsb = neigh & -neigh
                u = (lsb.bit_length() - 1)
                neigh ^= lsb
                if col[u] == 0:    # neighbour not coloured yet
                    if allowed[u] & bit:
                        allowed[u] ^= bit   # delete the bit
                        changed.append(u)
                        if allowed[u] == 0:
                            conflict = True
                            # no need to continue deleting, but we still
                            # have to finish the loop to keep neighbour mask
                # already coloured neighbours are already consistent
                # because their colour was removed from allowed[v] earlier

            if not conflict:
                if dfs(v + 1):
                    return True

            # undo the deletions
            for u in changed:
                allowed[u] |= bit
            col[v] = 0

        return False

    if dfs(0):
        out = "YES\n" + " ".join(str(c) for c in col)
        sys.stdout.write(out)
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()