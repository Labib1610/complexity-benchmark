import sys
sys.setrecursionlimit(100000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0]*(n+1)
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx > n:
            return True
        for c in (1,2,3):
            # check conflicts with already colored neighbors
            ok = True
            for nb in adj[idx]:
                if nb < idx and color[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            color[idx] = c
            if dfs(idx+1):
                return True
            color[idx] = 0
        return False

    if dfs(1):
        out = ["YES", " ".join(str(color[i]) for i in range(1, n+1))]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()