import sys

def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neigh[u].append(v)
        neigh[v].append(u)

    color = [0] * n          # 0 unassigned, 1..3 assigned
    allowed = [0b111] * n    # 3-bit mask for each vertex

    def dfs(idx):
        if idx == n:
            return True
        # if no color possible, prune
        if allowed[idx] == 0:
            return False
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (allowed[idx] & bit):
                continue
            color[idx] = c
            changes = []
            conflict = False
            for j in neigh[idx]:
                if color[j] == 0:
                    prev = allowed[j]
                    allowed[j] &= ~bit
                    changes.append((j, prev))
                    if allowed[j] == 0:
                        conflict = True
                        break
            if not conflict:
                if dfs(idx + 1):
                    return True
            # revert changes
            for j, prev in changes:
                allowed[j] = prev
            color[idx] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(str(c) for c in color)]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()