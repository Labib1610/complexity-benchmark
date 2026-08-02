import sys

def main():
    sys.setrecursionlimit(1000000)
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

    color = [0] * n          # 0 = uncolored, 1..3 = colors
    domains = [7] * n        # bitmask 0b111 for colors 1,2,3

    def dfs(idx):
        if idx == n:
            return True
        dom = domains[idx]
        for c in range(1, 4):
            bit = 1 << (c - 1)
            if not (dom & bit):
                continue
            # conflict with already colored neighbors
            conflict = False
            for nb in adj[idx]:
                if nb < idx and color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue

            color[idx] = c
            changes = []
            ok = True
            for nb in adj[idx]:
                if nb > idx:
                    if domains[nb] & bit:
                        prev = domains[nb]
                        domains[nb] &= ~bit
                        changes.append((nb, prev))
                        if domains[nb] == 0:
                            ok = False
                            break
            if ok:
                if dfs(idx + 1):
                    return True
            # revert
            for nb, prev in changes:
                domains[nb] = prev
            color[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(map(str, color))]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()