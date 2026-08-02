import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    avail = [0b111] * (n + 1)  # 3-bit mask for colors 1-3
    assign = [0] * (n + 1)

    def dfs(i: int) -> bool:
        if i > n:
            return True
        for color in (1, 2, 3):
            bit = 1 << (color - 1)
            # check conflict with already colored neighbors
            conflict = False
            for nb in adj[i]:
                if nb < i and assign[nb] == color:
                    conflict = True
                    break
            if conflict:
                continue

            # forward-check: update avail for uncolored neighbors > i
            updates = []
            prune = False
            for nb in adj[i]:
                if nb > i:
                    old = avail[nb]
                    new = old & ~bit
                    if new == 0:
                        prune = True
                    updates.append((nb, old))
                    avail[nb] = new
            if prune:
                # restore
                for nb, old in updates:
                    avail[nb] = old
                continue

            assign[i] = color
            if dfs(i + 1):
                return True
            assign[i] = 0
            # restore avail
            for nb, old in updates:
                avail[nb] = old
        return False

    if dfs(1):
        out = ['YES', '\n', ' '.join(str(assign[i]) for i in range(1, n + 1))]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()