import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        adj[b].append(a)

    color = [0] * n  # 0 means uncolored, otherwise 1..3

    def dfs(idx):
        if idx == n:
            return True
        v = idx
        # Try colors 1..3
        for c in (1, 2, 3):
            # Check conflict with already colored neighbors
            conflict = False
            for nb in adj[v]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            # Assign color
            color[v] = c
            # Update allowed set for uncolored neighbors
            changed = []
            ok = True
            for nb in adj[v]:
                if color[nb] == 0:
                    # If this neighbor will no longer have any color options, prune
                    # Remove color c from its allowed set
                    # We don't need to keep track of the set explicitly; just mark that if it becomes empty, we cannot proceed
                    # So we reduce a counter or check later
                    # We'll use a simple counter approach: if any neighbor has no options after removal, prune
                    # But since we don't maintain the set explicitly, we check when we reach that vertex
                    pass
            # Actually, we can use a simple heuristic: if any uncolored vertex ends up with no possible colors after this assignment, we will detect it when that vertex's turn comes.
            # So we don't need to modify allowed sets here. We'll just rely on the fact that we cannot assign the same color to a neighbor later.
            # The DFS will handle contradictions.
            if dfs(idx + 1):
                return True
            # Backtrack
            color[v] = 0
        return False

    # The above naive DFS doesn't use allowed pruning, but it's enough for n <= 40?
    # However, to ensure pruning, we will use a more aggressive approach with allowed counts.
    # Let's implement a refined version:

    # Re-implement with allowed sets
    allowed = [0b111 for _ in range(n)]  # 3 bits for colors 1,2,3

    def dfs2(idx):
        if idx == n:
            return True
        v = idx
        for c in (1, 2, 3):
            # Check conflict with colored neighbors
            conflict = False
            for nb in adj[v]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            # Assign color
            color[v] = c
            # Update allowed sets of neighbors
            changed = []
            for nb in adj[v]:
                if color[nb] == 0:
                    if (allowed[nb] >> (c - 1)) & 1:
                        allowed[nb] &= ~(1 << (c - 1))
                        changed.append(nb)
                        if allowed[nb] == 0:
                            # neighbor has no colors left -> backtrack
                            conflict = True
                            break
            if conflict:
                # Restore allowed sets
                for nb in changed:
                    allowed[nb] |= (1 << (c - 1))
                color[v] = 0
                continue
            if dfs2(idx + 1):
                return True
            # Backtrack
            for nb in changed:
                allowed[nb] |= (1 << (c - 1))
            color[v] = 0
        return False

    if dfs2(0):
        sys.stdout.write(" ".join(str(x) for x in color))
    else:
        sys.stdout.write("-1")

if __name__ == "__main__":
    solve()