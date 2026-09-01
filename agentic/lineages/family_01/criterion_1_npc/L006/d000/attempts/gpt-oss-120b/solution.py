import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # domains as 3-bit mask, bit 0->color1,1->color2,2->color3
    domains = [0b111] * n
    assign = [0] * n  # 0 means unassigned, else 1..3

    # stack for backtracking changes: list of (vertex, old_mask)
    changes = []

    sys.setrecursionlimit(10000)

    def dfs(v: int) -> bool:
        if v == n:
            return True
        # try colors 1..3
        for c in range(1, 4):
            mask = 1 << (c - 1)
            if not (domains[v] & mask):
                continue
            # assign
            assign[v] = c
            # record changes
            saved = []
            ok = True
            # propagate to neighbors
            nb = adj[v]
            u = 0
            while nb:
                lsb = nb & -nb
                u = (lsb.bit_length() - 1)
                nb ^= lsb
                if assign[u]:
                    if assign[u] == c:
                        ok = False
                        break
                else:
                    if domains[u] & mask:
                        old = domains[u]
                        new = old & ~mask
                        if new == 0:
                            ok = False
                            # revert later
                            saved.append((u, old))
                            break
                        saved.append((u, old))
                        domains[u] = new
            if ok:
                # push saved changes
                changes.extend(saved)
                if dfs(v + 1):
                    return True
                # revert saved
                for u, old in reversed(saved):
                    domains[u] = old
                del changes[-len(saved):]
            else:
                # revert partial saved
                for u, old in reversed(saved):
                    domains[u] = old
            assign[v] = 0
        return False

    possible = dfs(0)
    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(c) for c in assign))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()