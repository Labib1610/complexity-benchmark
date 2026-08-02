import sys
sys.setrecursionlimit(10000)

def main():
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
        if u != v:
            adj[u].add(v)
            adj[v].add(u)

    colors = [0] * n

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if nb < idx and colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                if dfs(idx + 1):
                    return True
        colors[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    main()