import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Sort vertices by degree (ascending) for better pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"))
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    # Rebuild adjacency in sorted order
    new_adj = [0] * n
    for i in range(n):
        mask = 0
        for j in range(n):
            if (adj[order[i]] >> order[j]) & 1:
                mask |= (1 << j)
        new_adj[i] = mask

    available = (1 << n) - 1
    chosen = []

    def backtrack(start, chosen_count, avail_mask):
        if chosen_count == k:
            return True
        if start >= n:
            return False
        # Prune: not enough remaining vertices
        if n - start < k - chosen_count:
            return False

        # Try to pick vertex at position 'start' if available
        if (avail_mask >> start) & 1:
            chosen.append(order[start])
            new_avail = avail_mask & ~new_adj[start] & ~(1 << start)
            if backtrack(start + 1, chosen_count + 1, new_avail):
                return True
            chosen.pop()

        # Skip this vertex
        if backtrack(start + 1, chosen_count, avail_mask):
            return True
        return False

    if backtrack(0, 0, available):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()