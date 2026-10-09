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

    # empty graph – any assignment works
    if m == 0:
        ans = [(i % 3) + 1 for i in range(n)]
        print("YES")
        print(*ans)
        return

    # masks: bit 0 -> colour 1, bit1 -> colour2, bit2 -> colour3
    ALL = 0b111
    possible = [ALL] * n
    colour = [0] * n          # 0 = uncoloured, else 1..3

    # static order for tie‑breaking (higher degree first)
    degree = [len(adj[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -degree[x])

    # symmetry breaking: first vertex gets colour 1
    first = 0
    colour[first] = 1
    possible[first] = 1 << 0
    for nb in adj[first]:
        if colour[nb] == 0:
            possible[nb] &= ~ (1 << 0)

    # helper: popcount of 3‑bit mask
    popcnt = [bin(i).count('1') for i in range(8)]

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # choose vertex with minimum remaining colours (MRV)
        v = -1
        best = 4
        for i in range(n):
            if colour[i] == 0:
                pc = popcnt[possible[i]]
                if pc < best:
                    best = pc
                    v = i
                    if pc == 1:
                        break
        if best == 0:          # dead end
            return False

        orig_mask = possible[v]
        # iterate over still possible colours
        for c in range(3):
            if not (orig_mask >> c) & 1:
                continue
            colour[v] = c + 1
            possible[v] = 1 << c
            changed = []
            conflict = False

            for nb in adj[v]:
                if colour[nb] == 0:
                    if possible[nb] & (1 << c):
                        possible[nb] &= ~(1 << c)
                        changed.append(nb)
                        if possible[nb] == 0:
                            conflict = True
                            break
            if not conflict and dfs(coloured_cnt + 1):
                return True

            # undo
            for nb in changed:
                possible[nb] |= (1 << c)
            colour[v] = 0
            possible[v] = orig_mask
        return False

    if dfs(1):
        print("YES")
        print(*colour)
    else:
        print("NO")

if __name__ == "__main__":
    solve()