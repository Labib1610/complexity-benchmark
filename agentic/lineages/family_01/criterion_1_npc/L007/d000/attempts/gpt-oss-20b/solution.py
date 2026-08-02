import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neighbors[u].append(v)
        neighbors[v].append(u)

    colors = [0] * n  # 0 unassigned, 1-3 assigned

    sys.setrecursionlimit(10000)

    def dfs(v):
        if v == n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for u in neighbors[v]:
                if colors[u] == c:
                    conflict = True
                    break
            if conflict:
                continue
            colors[v] = c
            if dfs(v + 1):
                return True
            colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    main()