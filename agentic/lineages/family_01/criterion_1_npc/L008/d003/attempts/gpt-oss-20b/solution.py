import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # available colors mask for each vertex (bits 0,1,2 for colors 1,2,3)
    ALL = 0b111
    avail = [ALL] * (n + 1)
    assign = [0] * (n + 1)

    def dfs(idx: int) -> bool:
        if idx > n:
            return True
        for color in (1, 2, 3):
            bit = 1 << (color - 1)
            if not (avail[idx] & bit):
                continue
            # check conflict with already assigned neighbors
            conflict = False
            for nb in adj[idx]:
                if nb < idx and assign[nb] == color:
                    conflict = True
                    break
            if conflict:
                continue
            # assign
            assign[idx] = color
            changes = []
            ok = True
            for nb in adj[idx]:
                if nb > idx:
                    if avail[nb] & bit:
                        old = avail[nb]
                        avail[nb] = old & ~bit
                        changes.append((nb, old))
                        if avail[nb] == 0:
                            ok = False
                            break
            if ok and dfs(idx + 1):
                return True
            # rollback
            for nb, old in changes:
                avail[nb] = old
            assign[idx] = 0
        return False

    if dfs(1):
        out = "YES\n" + " ".join(str(assign[i]) for i in range(1, n + 1))
        sys.stdout.write(out)
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()