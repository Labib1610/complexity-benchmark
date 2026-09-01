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

    color = [0] * n               # 0 = uncoloured, else 1..3
    allowed = [0b111] * n         # bits for colours 1,2,3

    # pre‑compute bit masks
    bit = [1 << 0, 1 << 1, 1 << 2]

    # depth‑first search
    def dfs(v: int) -> bool:
        if v == n:
            return True
        # try colours 1..3
        for c in (1, 2, 3):
            if not (allowed[v] & bit[c - 1]):
                continue
            conflict = False
            for nb in adj[v]:
                if nb < v and color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue

            # assign colour c to v
            color[v] = c
            saved = []          # (vertex, old_allowed)
            ok = True
            for nb in adj[v]:
                if nb > v:
                    old = allowed[nb]
                    new = old & ~bit[c - 1]
                    if new != old:
                        saved.append((nb, old))
                        allowed[nb] = new
                    if new == 0:
                        ok = False
                        break
            if ok and dfs(v + 1):
                return True
            # backtrack
            for nb, old in saved:
                allowed[nb] = old
            color[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()