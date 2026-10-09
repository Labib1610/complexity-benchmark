import sys

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

    # pre‑compute allowed ordered pairs
    ok = [[False] * 4 for _ in range(4)]   # 1..3
    for a in range(1, 4):
        for b in range(1, 4):
            if a == b:
                continue
            if a * a + (a + b) * (4 - a) != 16:
                ok[a][b] = True

    c = [0] * (n + 1)   # 1‑based

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n + 1:
            return True
        for val in (1, 2, 3):
            # check already assigned neighbours
            good = True
            for nb in adj[pos]:
                if c[nb] != 0 and not ok[val][c[nb]]:
                    good = False
                    break
            if not good:
                continue

            # forward checking: each unassigned neighbour must keep at least one colour
            feasible = True
            for nb in adj[pos]:
                if c[nb] == 0:
                    possible = False
                    for cand in (1, 2, 3):
                        if ok[cand][val]:
                            possible = True
                            break
                    if not possible:
                        feasible = False
                        break
            if not feasible:
                continue

            c[pos] = val
            if dfs(pos + 1):
                return True
            c[pos] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(c[i]) for i in range(1, n + 1))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()