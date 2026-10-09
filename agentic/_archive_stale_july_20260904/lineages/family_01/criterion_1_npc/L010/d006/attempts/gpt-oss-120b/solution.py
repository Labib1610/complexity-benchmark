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

    # colour of each vertex, 0 = uncoloured, otherwise 1..3
    color = [0] * n
    # allowed colours as bitmask, bit 0 -> colour 1, bit 1 -> colour 2, bit 2 -> colour 3
    allowed = [0b111] * n

    # depth‑first search
    def dfs(idx: int) -> bool:
        if idx == n:
            return True  # all coloured

        mask = allowed[idx]
        # try colours 1,2,3 in order
        for c in range(1, 4):
            bit = 1 << (c - 1)
            if not (mask & bit):
                continue

            # assign colour c to vertex idx
            color[idx] = c
            changed = []          # neighbours whose mask loses this colour
            conflict = False

            for nb in adj[idx]:
                if color[nb] != 0:          # already coloured neighbour – conflict already impossible because we checked allowed
                    continue
                if allowed[nb] & bit:
                    allowed[nb] ^= bit      # remove colour c
                    changed.append(nb)
                    if allowed[nb] == 0:    # no colour left -> dead end
                        conflict = True
                        break

            if not conflict:
                if dfs(idx + 1):
                    return True

            # backtrack: restore masks
            for nb in changed:
                allowed[nb] |= bit
            color[idx] = 0

        return False

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(c) for c in color))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()