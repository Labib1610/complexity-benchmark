import sys
sys.setrecursionlimit(1 << 20)

def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # If k is too large, impossible
    if k > n:
        print("NO")
        return

    # Try to find an independent set of size k
    # Use branch and bound with bitsets
    # We'll use a recursive search with pruning

    # Precompute for each vertex the set of vertices it conflicts with
    # We'll use a simple backtracking with bitsets

    # Sort vertices by degree (ascending) to improve pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'))
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    # Convert adjacency to new order
    new_adj = [0] * n
    for i in range(n):
        mask = 0
        for j in range(n):
            if (adj[order[i]] >> order[j]) & 1:
                mask |= (1 << j)
        new_adj[i] = mask

    # Search for independent set of size k
    # We'll use recursive function with current set, candidates, and remaining
    # candidates is a bitset of vertices that can still be added

    all_mask = (1 << n) - 1

    # Memoization for (candidates, remaining) -> bool
    # But n <= 46, so we can't memoize all states; we'll use pruning

    # Simple backtracking with bitsets
    def dfs(candidates, chosen_count):
        if chosen_count == k:
            return True
        # If not enough candidates left
        if bin(candidates).count('1') < k - chosen_count:
            return False
        # Choose a vertex with fewest candidates among remaining
        # To improve, pick vertex with smallest degree in the induced subgraph
        # We'll just pick the first set bit
        # But to be more efficient, pick vertex with smallest number of neighbors in candidates
        best_v = -1
        best_deg = n + 1
        c = candidates
        while c:
            lsb = c & -c
            v = (lsb.bit_length() - 1)
            deg = bin(new_adj[v] & candidates).count('1')
            if deg < best_deg:
                best_deg = deg
                best_v = v
                if deg == 0:
                    break
            c -= lsb
        v = best_v
        # Include v
        new_candidates = candidates & ~(1 << v) & ~new_adj[v]
        if dfs(new_candidates, chosen_count + 1):
            chosen.append(v)
            return True
        # Exclude v
        if dfs(candidates & ~(1 << v), chosen_count):
            return True
        return False

    chosen = []
    if dfs(all_mask, 0):
        # chosen is in reverse order
        chosen.reverse()
        # Map back to original labels
        ans = [order[v] + 1 for v in chosen]
        print("YES")
        print(" ".join(map(str, ans)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()