import sys

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
        if u == v:
            continue
        adj[u].add(v)
        adj[v].add(u)

    colors = [0] * n          # 0 = unassigned, else 1..3
    avail = [0b111] * n       # 3-bit mask for available colors

    sys.setrecursionlimit(10000)

    def dfs(idx):
        if idx == n:
            return True
        node = idx
        for color in (1, 2, 3):
            if not (avail[node] >> (color - 1)) & 1:
                continue
            colors[node] = color
            affected = []
            ok = True
            for nb in adj[node]:
                if colors[nb] == 0:
                    prev = avail[nb]
                    new = prev & ~(1 << (color - 1))
                    if new == 0:
                        ok = False
                        break
                    if new != prev:
                        avail[nb] = new
                        affected.append((nb, prev))
            if ok and dfs(idx + 1):
                return True
            # restore
            for nb, prev in affected:
                avail[nb] = prev
            colors[node] = 0
        return False

    if dfs(0):
        out = ["YES"]
        out.append(" ".join(str(c) for c in colors))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()