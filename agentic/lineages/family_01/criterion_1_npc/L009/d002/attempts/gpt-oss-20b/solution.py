import sys

def main():
    sys.setrecursionlimit(10000)
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
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)

    color = [0] * (n + 1)

    def dfs(idx):
        if idx > n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[idx]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[idx] = c
            # forward checking
            ok = True
            for u in range(idx + 1, n + 1):
                used = 0
                for nb in adj[u]:
                    if color[nb]:
                        used |= 1 << (color[nb] - 1)
                    if used == 0b111:
                        break
                if used == 0b111:
                    ok = False
                    break
            if ok and dfs(idx + 1):
                return True
            color[idx] = 0
        return False

    if dfs(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    main()