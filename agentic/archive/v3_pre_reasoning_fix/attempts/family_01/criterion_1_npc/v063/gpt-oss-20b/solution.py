import sys

def main():
    sys.setrecursionlimit(10000)
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

    avail = [0b111] * n          # 3 colors available initially
    colored = [-1] * n
    solution = None

    def dfs(idx):
        nonlocal solution
        if idx == n:
            solution = colored.copy()
            return True
        node = idx
        for col in range(3):
            if avail[node] & (1 << col):
                colored[node] = col
                changes = []
                fail = False
                for nb in adj[node]:
                    if colored[nb] == -1:
                        old = avail[nb]
                        new = old & ~(1 << col)
                        if old != new:
                            changes.append((nb, old))
                            avail[nb] = new
                            if new == 0:
                                fail = True
                                break
                if not fail:
                    if dfs(idx + 1):
                        return True
                # backtrack
                for nb, old in changes:
                    avail[nb] = old
                colored[node] = -1
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c + 1) for c in solution))
    else:
        print("NO")

if __name__ == "__main__":
    main()