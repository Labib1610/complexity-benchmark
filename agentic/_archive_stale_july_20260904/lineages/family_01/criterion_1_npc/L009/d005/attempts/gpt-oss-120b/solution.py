import sys
sys.setrecursionlimit(1000000)

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

    mask = [0b111] * n          # bits 0,1,2 -> colours 1,2,3
    col = [0] * n               # 0 = not assigned yet
    answer = None               # will hold the final sequence

    def dfs(pos: int) -> bool:
        nonlocal answer
        if pos == n:
            answer = col.copy()
            return True

        # try colours 1,2,3 in order
        for colour in (1, 2, 3):
            bit = 1 << (colour - 1)
            if not (mask[pos] & bit):
                continue

            # assign
            col[pos] = colour
            changed = []          # list of (vertex, old_mask)
            ok = True

            for nb in adj[pos]:
                if col[nb] == 0:
                    if mask[nb] & bit:
                        old = mask[nb]
                        new = old & ~bit
                        changed.append((nb, old))
                        mask[nb] = new
                        if new == 0:
                            ok = False
                            break

            if ok and dfs(pos + 1):
                return True

            # revert
            for v, old in reversed(changed):
                mask[v] = old
            col[pos] = 0

        return False

    if dfs(0):
        out = ['YES', ' '.join(str(x) for x in answer)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()