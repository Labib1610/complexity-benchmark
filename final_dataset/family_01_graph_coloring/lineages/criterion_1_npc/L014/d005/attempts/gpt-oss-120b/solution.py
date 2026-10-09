import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    colors = [-1] * n
    order = sorted(range(n), key=lambda x: -len(adj[x]))  # static order by degree

    # For dynamic selection we can pick first uncolored in order
    def backtrack(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        for c in range(3):
            ok = True
            for nb in adj[v]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[v] = c
                if backtrack(pos + 1):
                    return True
                colors[v] = -1
        return False

    if backtrack(0):
        print("YES")
        # map 0,1,2 to 1,2,3
        print(' '.join(str(c + 1) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()