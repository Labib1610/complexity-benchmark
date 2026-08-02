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

    colors = [0] * n
    sys.setrecursionlimit(1000000)

    def dfs(idx):
        if idx == n:
            return True
        forbidden = [False] * 4  # indices 1..3
        for nb in adj[idx]:
            c = colors[nb]
            if c:
                forbidden[c] = True
        for c in (1, 2, 3):
            if not forbidden[c]:
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