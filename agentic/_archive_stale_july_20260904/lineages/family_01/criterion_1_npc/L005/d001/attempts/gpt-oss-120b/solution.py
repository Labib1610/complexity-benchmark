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

    # colour[i] = 0 (uncoloured) or 1..3
    colour = [0] * n
    ALL = 0b111  # bits for colours 1,2,3
    allowed0 = [ALL] * n

    # depth‑first search with fixed order 0..n-1
    def dfs(i: int, allowed):
        if i == n:
            return True
        mask = allowed[i]
        if mask == 0:
            return False
        for c in (1, 2, 3):          # try colours increasingly
            bit = 1 << (c - 1)
            if not (mask & bit):
                continue
            # copy allowed, assign colour
            new_allowed = allowed[:]      # length <= 40, cheap
            colour[i] = c
            ok = True
            for nb in adj[i]:
                if colour[nb] == 0:       # neighbour still uncoloured
                    new_allowed[nb] &= ~bit
                    if new_allowed[nb] == 0:
                        ok = False
                        break
            if ok and dfs(i + 1, new_allowed):
                return True
            colour[i] = 0                 # backtrack
        return False

    if dfs(0, allowed0):
        out = ['YES', ' '.join(str(c) for c in colour)]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()