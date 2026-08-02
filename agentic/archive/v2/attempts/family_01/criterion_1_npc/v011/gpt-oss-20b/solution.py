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
        if v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)

    allowed = [7] * n          # bits 0,1,2 for colors 1,2,3
    assigned = [0] * n
    result = []

    def backtrack(idx: int) -> bool:
        if idx == n:
            result.extend(assigned)
            return True
        bitmask = allowed[idx]
        for color in range(1, 4):
            bit = 1 << (color - 1)
            if not (bitmask & bit):
                continue
            # assign
            assigned[idx] = color
            removed = []
            for nb in adj[idx]:
                if assigned[nb] == 0 and (allowed[nb] & bit):
                    allowed[nb] ^= bit
                    removed.append(nb)
                    if allowed[nb] == 0:
                        # dead end
                        break
            else:
                # continue recursion only if no dead end
                if backtrack(idx + 1):
                    return True
            # backtrack changes
            for nb in removed:
                allowed[nb] ^= bit
            assigned[idx] = 0
        return False

    if backtrack(0):
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()