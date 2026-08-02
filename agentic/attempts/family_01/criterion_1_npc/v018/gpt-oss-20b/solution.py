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
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    colors = [0] * n          # 0 = uncolored, else 1/2/3
    avail = [0b111] * n       # bitmask of available colors for each uncolored node
    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        for col in (1, 2, 3):
            if not (avail[pos] & (1 << (col - 1))):
                continue
            colors[pos] = col
            changed = []
            fail = False
            for nb in adj[pos]:
                if colors[nb] == 0:
                    prev = avail[nb]
                    new = prev & ~(1 << (col - 1))
                    if new == 0:
                        fail = True
                        break
                    if new != prev:
                        avail[nb] = new
                        changed.append((nb, prev))
            if not fail:
                if dfs(pos + 1):
                    return True
            # backtrack
            colors[pos] = 0
            for nb, prev in changed:
                avail[nb] = prev
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    main()