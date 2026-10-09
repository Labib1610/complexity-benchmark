import sys

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

    color = [0] * n               # 0 = uncoloured, else 1..3
    forb = [0] * n                # 3‑bit mask of forbidden colours
    stack = []                    # (vertex, previous_mask)

    ALL = 7                       # 0b111, all three colours forbidden

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True

        v = pos
        available = ALL ^ forb[v]          # colours not yet forbidden
        for c in range(3):                 # try colours 1,2,3
            bit = 1 << c
            if not (available & bit):
                continue

            # assign colour c+1 to vertex v
            color[v] = c + 1
            saved_len = len(stack)
            conflict = False

            for u in adj[v]:
                if color[u] != 0:          # neighbour already coloured
                    continue
                prev = forb[u]
                new = prev | bit
                if new != prev:
                    stack.append((u, prev))
                    forb[u] = new
                    if new == ALL:          # u lost all possible colours
                        conflict = True
                        break

            if not conflict and dfs(pos + 1):
                return True

            # backtrack: restore masks and colour
            while len(stack) > saved_len:
                u, prev = stack.pop()
                forb[u] = prev
            color[v] = 0

        return False

    if dfs(0):
        out = "YES\n" + " ".join(str(c) for c in color) + "\n"
    else:
        out = "NO\n"
    sys.stdout.write(out)


if __name__ == "__main__":
    solve()