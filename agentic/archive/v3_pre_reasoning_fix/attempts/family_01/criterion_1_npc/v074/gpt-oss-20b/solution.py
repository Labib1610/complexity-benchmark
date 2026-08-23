import sys

def main():
    sys.setrecursionlimit(1000000)
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

    def dfs(i):
        if i == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for j in adj[i]:
                if j < i and color[j] == c:
                    ok = False
                    break
            if not ok:
                continue
            color[i] = c
            if dfs(i + 1):
                return True
            color[i] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()