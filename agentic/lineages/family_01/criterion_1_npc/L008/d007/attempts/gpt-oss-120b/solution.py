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

    # 0 = uncoloured, otherwise 1..3
    colour = [0] * n
    # mask of possible colours, bit 0 -> colour 1, bit1 -> colour2, bit2 -> colour3
    possible = [0b111] * n

    # depth‑first search, vertices are processed in order 0..n-1
    def dfs(v: int) -> bool:
        # skip already coloured vertices (should not happen, but keep it safe)
        while v < n and colour[v] != 0:
            v += 1
        if v == n:          # all vertices coloured
            return True

        mask = possible[v]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if mask & bit == 0:
                continue

            # assign colour c to vertex v
            colour[v] = c
            changed = []          # list of (vertex, old_mask) to undo
            ok = True

            for nb in adj[v]:
                if colour[nb] == 0:
                    if possible[nb] & bit:
                        old = possible[nb]
                        new = old & ~bit
                        if new != old:
                            changed.append((nb, old))
                            possible[nb] = new
                            if new == 0:
                                ok = False
                                break
            if ok:
                if dfs(v + 1):
                    return True

            # undo changes
            for nb, old in reversed(changed):
                possible[nb] = old
            colour[v] = 0

        return False

    if dfs(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(colour[i]) for i in range(n)))
        sys.stdout.write("\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()