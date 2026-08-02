import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    colors = [0] * n          # 0 = unassigned, 1/2/3 assigned
    color_masks = [0, 0, 0, 0]  # index 1..3

    sys.setrecursionlimit(10000)

    def dfs(pos):
        if pos == n:
            return True
        for c in (1, 2, 3):
            if (adj_mask[pos] & color_masks[c]) == 0:
                colors[pos] = c
                color_masks[c] |= 1 << pos
                # forward checking
                ok = True
                for nb in neighbors[pos]:
                    if colors[nb] == 0:
                        avail = False
                        for cc in (1, 2, 3):
                            if (adj_mask[nb] & color_masks[cc]) == 0:
                                avail = True
                                break
                        if not avail:
                            ok = False
                            break
                if ok and dfs(pos + 1):
                    return True
                # backtrack
                colors[pos] = 0
                color_masks[c] &= ~(1 << pos)
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(map(str, colors))]
    else:
        out_lines = ["NO"]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()