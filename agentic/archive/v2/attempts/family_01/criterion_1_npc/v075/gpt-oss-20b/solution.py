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
        u = int(next(it)) - 1   # 0‑based
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    colour = [0] * n                   # 0 = uncoloured
    used   = [[0, 0, 0] for _ in range(n)]   # used[v][c]  for v > current

    def dfs(i: int) -> bool:
        if i == n:                     # all vertices coloured
            return True

        for c in (1, 2, 3):
            # conflict with already coloured neighbours ?
            conflict = False
            for nb in adj[i]:
                if nb < i and colour[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue

            # assign colour
            colour[i] = c
            affected = []

            for nb in adj[i]:
                if nb > i:
                    used[nb][c - 1] += 1
                    affected.append(nb)

            # forward checking
            possible = True
            for v in range(i + 1, n):
                if used[v][0] > 0 and used[v][1] > 0 and used[v][2] > 0:
                    possible = False
                    break

            if possible and dfs(i + 1):
                return True

            # backtrack
            colour[i] = 0
            for v in affected:
                used[v][c - 1] -= 1

        return False

    if dfs(0):
        print(" ".join(map(str, colour)))
    else:
        print("impossible")

if __name__ == "__main__":
    solve()