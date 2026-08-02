import sys
sys.setrecursionlimit(1000)

# -------------------------------------------------------------

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)

    # adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    colour = [0] * n               # 0 = uncoloured, else 1/2/3
    avail = [0b111] * n            # 3 bits, all colours initially possible

    # colour bits and their indices (bit 0 -> colour 1, etc.)
    colour_bits = [(1, 1), (2, 2), (4, 3)]

    def dfs(pos: int) -> bool:
        """Depth first search, next vertex to colour is 'pos'."""
        if pos == n:                 # all vertices coloured
            return True

        v = pos
        for bit, idx in colour_bits:
            if avail[v] & bit:       # this colour is still possible
                colour[v] = idx
                changed = []         # neighbours whose avail was updated
                ok = True

                for u in adj[v]:
                    if colour[u] == 0:          # u is still uncoloured
                        if avail[u] & bit:
                            old = avail[u]
                            avail[u] ^= bit       # forbid this colour
                            changed.append((u, old))
                            if avail[u] == 0:    # dead end
                                ok = False
                                break

                if ok and dfs(pos + 1):
                    return True          # success deep inside

                # revert all changes of this branch
                for u, old in changed:
                    avail[u] = old
                colour[v] = 0

        return False                    # no colour works for vertex v

    possible = dfs(0)

    out_lines = sys.stdout
    if not possible:
        out_lines.write("NO")
    else:
        out_lines.write("\n".join(map(str, colour)))

# -------------------------------------------------------------
if __name__ == "__main__":
    solve()