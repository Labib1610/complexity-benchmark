import sys

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

    # allowed colors bitmask: bit c (1..3) set means allowed
    allowed = [0b1110] * n  # bits 1,2,3 (ignore bit0)
    color = [0] * n
    sys.setrecursionlimit(10000)

    # order is fixed 0..n-1 to get lexicographically minimal
    def dfs(v: int) -> bool:
        if v == n:
            return True
        # try colors 1..3 in order
        for c in (1, 2, 3):
            if not (allowed[v] >> c) & 1:
                continue
            # assign
            color[v] = c
            # record changes to allowed of neighbors
            changed = []
            ok = True
            mask = 1 << c
            for nb in adj[v]:
                if color[nb] == 0:  # uncolored
                    if allowed[nb] & mask:
                        allowed[nb] ^= mask
                        changed.append(nb)
                        if allowed[nb] & 0b1110 == 0:
                            ok = False
                            break
                else:
                    if color[nb] == c:
                        ok = False
                        break
            if ok and dfs(v + 1):
                return True
            # backtrack
            for nb in changed:
                allowed[nb] |= mask
            color[v] = 0
        return False

    possible = dfs(0)
    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(c) for c in color))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()