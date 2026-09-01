import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    colour = [0] * n          # 0 = uncoloured, otherwise 1,2,3

    # ------------------------------------------------------------
    def dfs(v: int) -> bool:
        """try to colour vertices v .. n-1, return True on success"""
        if v == n:
            return True

        # colours forbidden by already coloured neighbours
        forbidden = {colour[w] for w in adj[v] if colour[w] != 0}

        for c in (1, 2, 3):
            if c in forbidden:
                continue
            colour[v] = c

            # forward check: any uncoloured neighbour already blocked?
            ok = True
            for u in adj[v]:
                if colour[u] != 0:
                    continue
                forb_u = {colour[w] for w in adj[u] if colour[w] != 0}
                if len(forb_u) == 3:          # no colour left for u
                    ok = False
                    break
            if ok and dfs(v + 1):
                return True
            colour[v] = 0                     # backtrack
        return False
    # ------------------------------------------------------------

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colour)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()