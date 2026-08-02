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

    color = [0] * n          # 0 = uncolored, 1-3 = colors
    allowed = [0b111] * n    # bitmask of allowed colors for each vertex

    def dfs(i: int) -> bool:
        if i == n:
            return True
        if allowed[i] == 0:
            return False
        for c in range(1, 4):
            if allowed[i] & (1 << (c - 1)):
                color[i] = c
                changed = []
                fail = False
                for nb in adj[i]:
                    if color[nb] == 0:
                        before = allowed[nb]
                        after = before & ~(1 << (c - 1))
                        if before != after:
                            allowed[nb] = after
                            changed.append((nb, before))
                            if after == 0:
                                fail = True
                                break
                if not fail:
                    if dfs(i + 1):
                        return True
                # restore
                for nb, before in changed:
                    allowed[nb] = before
                color[i] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(color[i]) for i in range(n))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()