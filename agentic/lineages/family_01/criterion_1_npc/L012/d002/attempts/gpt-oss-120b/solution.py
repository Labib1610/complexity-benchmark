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

    # 0 = uncoloured, otherwise 1,2,3
    col = [0] * n
    # bit mask of still possible colours, bits 0,1,2 = colours 1,2,3
    mask = [0b111] * n

    # depth‑first search respecting lexicographic order
    def dfs(v: int) -> bool:
        if v == n:
            return True

        # possible colours for this vertex, respecting current mask
        possible = []
        msk = mask[v]
        for c in (1, 2, 3):
            if msk & (1 << (c - 1)):
                # conflict with already coloured neighbours?
                conflict = False
                for nb in adj[v]:
                    if col[nb] == c:
                        conflict = True
                        break
                if not conflict:
                    possible.append(c)

        for c in possible:
            col[v] = c
            changed = []          # list of (vertex, old_mask)
            ok = True
            bit = 1 << (c - 1)

            # remove colour c from masks of uncoloured neighbours
            for nb in adj[v]:
                if col[nb] == 0:
                    old = mask[nb]
                    if old & bit:
                        new = old & ~bit
                        if new == 0:
                            ok = False
                        changed.append((nb, old))
                        mask[nb] = new
            if ok and dfs(v + 1):
                return True

            # backtrack: restore masks
            for nb, old in reversed(changed):
                mask[nb] = old
            col[v] = 0

        return False

    if dfs(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(c) for c in col) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()