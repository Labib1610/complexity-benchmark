import sys
sys.setrecursionlimit(10000)

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n          # 0 = uncolored, 1/2/3 = slot
    allowed = [0b111] * n    # bitmask of allowed colors for each node

    def dfs():
        # find first uncolored node
        for i in range(n):
            if color[i] == 0:
                break
        else:
            return True  # all colored

        for val in (1, 2, 3):
            if not (allowed[i] & (1 << (val - 1))):
                continue
            color[i] = val
            changes = []
            ok = True
            for j in adj[i]:
                if color[j] == 0:
                    old = allowed[j]
                    new = old & ~(1 << (val - 1))
                    if new == 0:
                        ok = False
                        break
                    if new != old:
                        changes.append((j, old))
                        allowed[j] = new
            if ok and dfs():
                return True
            # backtrack
            for j, old in reversed(changes):
                allowed[j] = old
            color[i] = 0
        return False

    if dfs():
        out = ["YES", " ".join(map(str, color))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()