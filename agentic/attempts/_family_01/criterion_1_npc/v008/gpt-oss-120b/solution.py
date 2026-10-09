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

    # 3-bit masks, bit 0 -> colour 0 (shift 1), etc.
    domain = [0b111] * n
    colour = [-1] * n
    changes = []                     # stack of (v, old_mask, old_colour)

    # ------------------------------------------------------------
    def assign(v: int, col: int) -> bool:
        """try to set vertex v to colour col, with propagation.
           returns True iff no conflict."""
        if colour[v] != -1:
            return colour[v] == col
        if not (domain[v] >> col) & 1:
            return False

        # set domain to single colour and colour it
        changes.append((v, domain[v], colour[v]))
        domain[v] = 1 << col
        colour[v] = col

        queue = [v]
        while queue:
            x = queue.pop()
            cx = colour[x]
            for u in adj[x]:
                if colour[u] == -1:
                    if (domain[u] >> cx) & 1:
                        old_mask = domain[u]
                        new_mask = old_mask & ~(1 << cx)
                        if new_mask != old_mask:
                            changes.append((u, old_mask, colour[u]))
                            domain[u] = new_mask
                            if new_mask == 0:
                                return False
                            # unit propagation
                            if (new_mask & (new_mask - 1)) == 0:
                                c2 = new_mask.bit_length() - 1
                                colour[u] = c2
                                queue.append(u)
                else:
                    if colour[u] == cx:
                        return False
        return True
    # ------------------------------------------------------------

    def dfs() -> bool:
        # all coloured ?
        if all(c != -1 for c in colour):
            return True

        # choose vertex with smallest domain (>1)
        v = -1
        best = 4
        for i in range(n):
            if colour[i] == -1:
                sz = (domain[i] & 1) + ((domain[i] >> 1) & 1) + ((domain[i] >> 2) & 1)
                if sz < best:
                    best = sz
                    v = i
                    if sz == 2:
                        break

        mask = domain[v]
        for c in range(3):
            if (mask >> c) & 1:
                saved = len(changes)
                if assign(v, c):
                    if dfs():
                        return True
                # rollback
                while len(changes) > saved:
                    vv, old_mask, old_col = changes.pop()
                    domain[vv] = old_mask
                    colour[vv] = old_col
        return False

    possible = dfs()
    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(colour[i] + 1) for i in range(n)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()