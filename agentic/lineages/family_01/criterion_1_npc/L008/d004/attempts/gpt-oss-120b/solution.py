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

    # domain masks: bit 0->color1, 1->color2, 2->color3
    domain = [0b111] * n
    color = [0] * n  # 0 = unassigned, else 1..3

    # helper to count bits
    bitcnt = lambda x: (x & 1) + ((x>>1) & 1) + ((x>>2) & 1)

    # assign a vertex, record changes for backtrack
    def assign(v, col, changes):
        # set color
        changes.append(('col', v, color[v]))
        color[v] = col
        # set domain to single color
        changes.append(('dom', v, domain[v]))
        domain[v] = 1 << (col - 1)

        # propagate to neighbors
        mask = 1 << (col - 1)
        for nb in adj[v]:
            if color[nb] == 0 and (domain[nb] & mask):
                changes.append(('dom', nb, domain[nb]))
                domain[nb] &= ~mask
                if domain[nb] == 0:
                    return False
        return True

    # recursive dfs
    def dfs():
        # check if all assigned
        if all(c != 0 for c in color):
            return True

        # pick smallest unassigned vertex
        v = next(i for i, c in enumerate(color) if c == 0)

        # try colors in order 1..3 that are allowed
        for col in (1, 2, 3):
            if not (domain[v] & (1 << (col - 1))):
                continue
            changes = []
            ok = assign(v, col, changes)
            if not ok:
                # revert
                for typ, idx, prev in reversed(changes):
                    if typ == 'col':
                        color[idx] = prev
                    else:
                        domain[idx] = prev
                continue

            # propagate forced assignments (domains of size 1)
            forced = True
            while forced:
                forced = False
                for i in range(n):
                    if color[i] == 0 and bitcnt(domain[i]) == 1:
                        forced_col = (domain[i] & -domain[i]).bit_length()
                        # forced_col is 1..3
                        if not assign(i, forced_col, changes):
                            forced = False
                            break
                        forced = True
                if not forced:
                    break

            if dfs():
                return True
            # backtrack
            for typ, idx, prev in reversed(changes):
                if typ == 'col':
                    color[idx] = prev
                else:
                    domain[idx] = prev
        return False

    possible = dfs()
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(c) for c in color))

if __name__ == "__main__":
    solve()