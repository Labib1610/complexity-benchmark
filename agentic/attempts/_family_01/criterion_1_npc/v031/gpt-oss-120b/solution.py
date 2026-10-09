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
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    # domain[i]: bitmask of possible colors (bits 0,1,2 for colors 1,2,3)
    domain = [0b111] * n
    assigned = [0] * n  # 0 = unassigned, else 1..3

    # Pre‑order vertices by degree for tie‑breaking (higher degree first)
    degree = [len(adj[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -degree[x])

    # Helper to pick next vertex: MRV with tie‑break by degree
    def select_vertex() -> int:
        v = -1
        best = 4  # larger than max domain size (3)
        for i in range(n):
            if assigned[i] == 0:
                sz = domain[i].bit_count()
                if sz < best or (sz == best and degree[i] > degree[v]):
                    best = sz
                    v = i
                    if best == 1:
                        break
        return v

    def dfs() -> bool:
        v = select_vertex()
        if v == -1:          # all assigned
            return True

        cur_dom = domain[v]
        # try each possible color
        for c in range(3):
            if not (cur_dom & (1 << c)):
                continue
            assigned[v] = c + 1
            changed = []      # (neighbor, old_domain)
            fail = False

            for nb in adj[v]:
                if assigned[nb] == 0:
                    if domain[nb] & (1 << c):
                        old = domain[nb]
                        new = old & ~(1 << c)
                        changed.append((nb, old))
                        domain[nb] = new
                        if new == 0:
                            fail = True
                            break

            if not fail and dfs():
                return True

            # revert changes
            for nb, old in reversed(changed):
                domain[nb] = old
            assigned[v] = 0
        return False

    possible = dfs()
    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(col) for col in assigned))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()