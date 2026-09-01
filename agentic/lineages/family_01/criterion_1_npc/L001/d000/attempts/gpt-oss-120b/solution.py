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

    color = [0] * n               # 0 = uncoloured, 1..3 = work period

    # -----------------------------------------------------------------
    # feasibility test for the current partial colouring
    def possible() -> bool:
        # find uncoloured vertex with the smallest number of admissible colours
        best_v = -1
        best_opts = None

        for v in range(n):
            if color[v] != 0:
                continue
            forbidden = 0
            for nb in adj[v]:
                c = color[nb]
                if c:
                    forbidden |= 1 << (c - 1)
            opts = []
            for c in (1, 2, 3):
                if not (forbidden & (1 << (c - 1))):
                    opts.append(c)
            if not opts:                     # no colour possible → dead end
                return False
            if best_v == -1 or len(opts) < len(best_opts):
                best_v = v
                best_opts = opts
                if len(best_opts) == 1:
                    break

        if best_v == -1:                     # everything coloured
            return True

        for c in best_opts:
            color[best_v] = c
            if possible():
                color[best_v] = 0
                return True
            color[best_v] = 0
        return False
    # -----------------------------------------------------------------

    # main loop – enforce lexicographic order
    for v in range(n):
        placed = False
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[v]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[v] = c
            if possible():
                placed = True
                break
            color[v] = 0
        if not placed:
            print("NO")
            return

    print("YES")
    print(' '.join(str(c) for c in color))

if __name__ == "__main__":
    solve()