import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q

    reactions = []
    reaction_masks = []
    cluster_to_reactions = [[] for _ in range(n + 1)]

    for idx in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        reactions.append((a, b, c))
        mask = (1 << (a - 1)) | (1 << (b - 1)) | (1 << (c - 1))
        reaction_masks.append(mask)
        cluster_to_reactions[a].append(idx)
        cluster_to_reactions[b].append(idx)
        cluster_to_reactions[c].append(idx)

    full_mask = (1 << n) - 1

    # Quick check: every cluster must appear in at least one reaction
    for cluster in range(1, n + 1):
        if not cluster_to_reactions[cluster]:
            print("NO")
            return

    selected = []

    def dfs(used_mask):
        if used_mask == full_mask:
            return True

        # Find the unused cluster with the fewest available reactions
        best_cluster = -1
        best_count = 10**9
        for cluster in range(1, n + 1):
            if (used_mask >> (cluster - 1)) & 1:
                continue
            cnt = 0
            for idx in cluster_to_reactions[cluster]:
                if not (used_mask & reaction_masks[idx]):
                    cnt += 1
            if cnt == 0:
                return False
            if cnt < best_count:
                best_count = cnt
                best_cluster = cluster
                if cnt == 1:
                    break

        # Try each reaction containing this cluster
        for idx in cluster_to_reactions[best_cluster]:
            if used_mask & reaction_masks[idx]:
                continue
            selected.append(idx)
            if dfs(used_mask | reaction_masks[idx]):
                return True
            selected.pop()
        return False

    if dfs(0):
        print("YES")
        for idx in selected:
            a, b, c = reactions[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()