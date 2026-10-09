import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbors
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    # domains: 3 bits, bit 0 for color 1, bit1 for 2, bit2 for3
    ALL = 0b111
    domain = [ALL] * n
    color = [0] * n  # 0 = uncolored, else 1..3

    # order vertices by degree for tie-breaking
    order = sorted(range(n), key=lambda x: -len(neighbors[x]))

    # helper to pick next vertex: uncolored with smallest domain size
    def select_vertex():
        best = -1
        best_sz = 4
        for v in order:
            if color[v] == 0:
                sz = domain[v].bit_count()
                if sz < best_sz:
                    best_sz = sz
                    best = v
                    if sz == 1:
                        break
        return best

    sys.setrecursionlimit(10000)
    stack = []  # record (vertex, previous_domain)

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        if v == -1:
            return False
        avail = domain[v]
        # try colors in order 1..3
        for c in (1, 2, 3):
            mask = 1 << (c - 1)
            if not (avail & mask):
                continue
            # assign
            color[v] = c
            # record changes to neighbors
            changed = []
            for u in neighbors[v]:
                if color[u] == 0 and (domain[u] & mask):
                    prev = domain[u]
                    new = prev & ~mask
                    if new == 0:
                        # revert changes
                        for uu, old in changed:
                            domain[uu] = old
                        color[v] = 0
                        break
                    domain[u] = new
                    changed.append((u, prev))
            else:
                # recurse
                if dfs(colored_cnt + 1):
                    return True
                # revert neighbor domains
                for uu, old in changed:
                    domain[uu] = old
            # revert assignment
            color[v] = 0
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(c) for c in color))

if __name__ == "__main__":
    solve()