import sys
sys.setrecursionlimit(10000)

def solve():
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

    color = [0] * n
    avail = [0b111] * n  # bitmask of allowed colors for each node

    def dfs(idx):
        if idx == n:
            return True
        for c in range(3):  # colors 0,1,2 representing 1,2,3
            # try color c for node idx
            # copy availability
            new_avail = avail[:]  # shallow copy of list
            ok = True
            for nb in adj[idx]:
                if color[nb] == 0:
                    new_avail[nb] &= ~(1 << c)
                    if new_avail[nb] == 0:
                        ok = False
                        break
            if not ok:
                continue
            color[idx] = c + 1
            nonlocal avail
            avail, old_avail = new_avail, avail
            if dfs(idx + 1):
                return True
            # backtrack
            avail = old_avail
            color[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(map(str, color))]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()