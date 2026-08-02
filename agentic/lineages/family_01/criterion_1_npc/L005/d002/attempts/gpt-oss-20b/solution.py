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

    colors = [0] * n          # 0 = uncolored, else 1..3
    avail = [0b111] * n       # bitmask of available colors

    sys.setrecursionlimit(10000)

    def dfs(idx):
        if idx == n:
            return True
        i = idx
        for c in (1, 2, 3):
            mask = 1 << (c - 1)
            if not (avail[i] & mask):
                continue
            conflict = False
            changes = []
            for j in adj[i]:
                if colors[j] == c:
                    conflict = True
                    break
                if colors[j] == 0:
                    prev = avail[j]
                    new = prev & ~mask
                    if new == 0:
                        conflict = True
                        break
                    avail[j] = new
                    changes.append((j, prev))
            if conflict:
                for j, prev in changes:
                    avail[j] = prev
                continue
            colors[i] = c
            if dfs(i + 1):
                return True
            colors[i] = 0
            for j, prev in changes:
                avail[j] = prev
        return False

    if dfs(0):
        out = ["YES", "\n"] + [" ".join(map(str, colors))]
        sys.stdout.write(out[0] + out[1] + out[2])
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()