import sys

def main():
    sys.setrecursionlimit(10000)
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
        adj[u].append(v)
        adj[v].append(u)

    assignment = [0] * n
    used = [0] * n  # bitmask of colors used by neighbors

    def dfs(idx):
        if idx == n:
            return True
        for color in (1, 2, 3):
            bit = 1 << (color - 1)
            if used[idx] & bit:
                continue
            assignment[idx] = color
            changes = []
            conflict = False
            for nb in adj[idx]:
                if assignment[nb] == 0:  # unassigned neighbor
                    old_mask = used[nb]
                    new_mask = old_mask | bit
                    if new_mask != old_mask:
                        changes.append((nb, old_mask))
                        used[nb] = new_mask
                        if new_mask == 0b111:  # all colors already used
                            conflict = True
                            break
            if not conflict:
                if dfs(idx + 1):
                    return True
            # revert changes
            for nb, old_mask in reversed(changes):
                used[nb] = old_mask
            assignment[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    main()