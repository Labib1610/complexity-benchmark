import sys

def main() -> None:
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

    colors = [0] * n  # 0 unassigned, 1..3 assigned

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[pos]:
                if nb < pos and colors[nb] == c:
                    conflict = True
                    break
            if not conflict:
                colors[pos] = c
                if dfs(pos + 1):
                    return True
                colors[pos] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(map(str, colors))]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()