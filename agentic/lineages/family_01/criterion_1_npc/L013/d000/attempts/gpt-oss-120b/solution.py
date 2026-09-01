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

    # possible colors bitmask: bit 0->color1, 1->color2, 2->color3
    possible = [0b111] * n
    color = [0] * n  # 0 means unassigned, else 1..3
    sys.setrecursionlimit(10000)

    # order is fixed 0..n-1 to guarantee lexicographic minimality
    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        # if already colored (should not happen), skip
        if color[idx]:
            return dfs(idx + 1)

        mask = possible[idx]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (mask & bit):
                continue
            # assign c to idx
            color[idx] = c
            changed = []  # list of (neighbor, previous_mask)
            fail = False
            for nb in adj[idx]:
                if color[nb]:
                    if color[nb] == c:
                        fail = True
                        break
                else:
                    prev = possible[nb]
                    new = prev & ~bit
                    if new != prev:
                        changed.append((nb, prev))
                        possible[nb] = new
                        if new == 0:
                            fail = True
                            break
            if not fail and dfs(idx + 1):
                return True
            # revert changes
            for nb, prev in reversed(changed):
                possible[nb] = prev
            color[idx] = 0
        return False

    if dfs(0):
        out = "YES\n" + " ".join(str(c) for c in color)
    else:
        out = "NO"
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()