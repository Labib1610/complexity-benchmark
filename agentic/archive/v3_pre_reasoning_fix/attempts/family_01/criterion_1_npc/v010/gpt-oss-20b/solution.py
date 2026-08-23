import sys

def main():
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

    colors = [0] * n  # 0 means uncolored, else 1..3

    sys.setrecursionlimit(1000000)

    def dfs(idx):
        if idx == n:
            return True
        v = idx
        for c in (1, 2, 3):
            conflict = False
            for u in adj[v]:
                if colors[u] == c:
                    conflict = True
                    break
            if conflict:
                continue
            colors[v] = c
            # forward check: ensure remaining vertices have at least one possible color
            fail = False
            for w in range(idx + 1, n):
                if colors[w] == 0:
                    avail = False
                    for col in (1, 2, 3):
                        ok = True
                        for u in adj[w]:
                            if colors[u] == col:
                                ok = False
                                break
                        if ok:
                            avail = True
                            break
                    if not avail:
                        fail = True
                        break
            if not fail:
                if dfs(idx + 1):
                    return True
            colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(x) for x in colors))
    else:
        print("NO")

if __name__ == "__main__":
    main()