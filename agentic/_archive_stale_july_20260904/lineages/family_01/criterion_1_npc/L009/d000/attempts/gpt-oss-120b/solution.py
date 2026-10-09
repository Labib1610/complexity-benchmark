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

    col = [0] * n                     # 0 = uncoloured, else 1..3

    # ------------------------------------------------------------
    def dfs(i: int) -> bool:
        """try to colour vertices i .. n-1, return True if possible"""
        if i == n:
            return True

        for c in (1, 2, 3):
            # neighbour conflict ?
            conflict = False
            for nb in adj[i]:
                if col[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue

            col[i] = c                     # assign

            # forward checking: any still uncoloured vertex blocked completely ?
            ok = True
            for j in range(i + 1, n):
                if col[j] != 0:
                    continue
                used = set()
                for nb in adj[j]:
                    cc = col[nb]
                    if cc:
                        used.add(cc)
                if len(used) == 3:        # all colours forbidden
                    ok = False
                    break

            if ok and dfs(i + 1):
                return True

            col[i] = 0                     # undo

        return False
    # ------------------------------------------------------------

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in col))
    else:
        print("NO")


if __name__ == "__main__":
    solve()