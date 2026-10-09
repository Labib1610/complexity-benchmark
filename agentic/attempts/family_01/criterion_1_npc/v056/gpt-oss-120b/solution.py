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

    # 0,1,2 are internal colors, output will be +1
    color = [-1] * n
    possible = [0b111] * n          # bits 0,1,2 set

    # pre‑compute popcount for 0..7 (tiny)
    popcnt = [bin(i).count('1') for i in range(8)]

    def dfs(colored: int) -> bool:
        if colored == n:
            return True

        # MRV: vertex with smallest number of possible colors
        v = -1
        best = 4
        for i in range(n):
            if color[i] == -1:
                pc = popcnt[possible[i]]
                if pc < best:
                    best = pc
                    v = i
                    if pc == 1:
                        break
        if best == 0:          # dead end
            return False

        avail = possible[v]
        # try each possible color
        for c in range(3):
            bit = 1 << c
            if not (avail & bit):
                continue

            # assign
            color[v] = c
            changes = []        # (vertex, old_possible)
            fail = False

            for nb in adj[v]:
                if color[nb] == -1 and (possible[nb] & bit):
                    old = possible[nb]
                    possible[nb] = old & ~bit
                    changes.append((nb, old))
                    if possible[nb] == 0:
                        fail = True
                        break

            if not fail and dfs(colored + 1):
                return True

            # backtrack
            for nb, old in changes:
                possible[nb] = old
            color[v] = -1

        return False

    ok = dfs(0)
    out = []
    if ok:
        out.append("YES")
        out.append(' '.join(str(c + 1) for c in color))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()