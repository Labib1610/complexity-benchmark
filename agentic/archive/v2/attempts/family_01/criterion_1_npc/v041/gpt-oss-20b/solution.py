import sys

def main():
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
        adj[u].append(v)
        adj[v].append(u)

    colors = [0] * (n + 1)  # 1-indexed

    sys.setrecursionlimit(10000)

    def dfs(idx):
        if idx > n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[idx]:
                if nb < idx and colors[nb] == c:
                    conflict = True
                    break
            if not conflict:
                colors[idx] = c
                if dfs(idx + 1):
                    return True
                colors[idx] = 0
        return False

    if dfs(1):
        out = ["YES"]
        out.append(' '.join(str(colors[i]) for i in range(1, n + 1)))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()