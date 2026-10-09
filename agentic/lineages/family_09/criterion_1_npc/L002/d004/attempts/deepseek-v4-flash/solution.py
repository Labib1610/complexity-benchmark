import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Split vertices into two halves
    half1 = n // 2
    half2 = n - half1
    # Map global vertex -> local index in half
    v1 = list(range(half1))
    v2 = list(range(half1, n))

    # Build local adjacency for each half
    adj1 = [0] * half1
    for i in range(half1):
        for j in range(half1):
            if (adj[v1[i]] >> v1[j]) & 1:
                adj1[i] |= 1 << j

    adj2 = [0] * half2
    for i in range(half2):
        for j in range(half2):
            if (adj[v2[i]] >> v2[j]) & 1:
                adj2[i] |= 1 << j

    # Enumerate all independent sets in half2, store by mask
    # We'll store for each mask the size and the actual mask
    size2 = [0] * (1 << half2)
    indep2 = [False] * (1 << half2)
    indep2[0] = True
    for mask in range(1 << half2):
        # check if independent
        ok = True
        for i in range(half2):
            if (mask >> i) & 1:
                if (adj2[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            indep2[mask] = True
            size2[mask] = bin(mask).count("1")

    # For each possible forbidden mask in half2, store the max size of an independent set avoiding it
    # forbidden mask means those vertices cannot be chosen
    best_size_for_forbidden = [-1] * (1 << half2)
    # We'll compute by iterating all independent sets and updating their allowed masks
    # allowed mask = complement of forbidden
    for mask in range(1 << half2):
        if indep2[mask]:
            # This set avoids any forbidden that is subset of complement(mask)
            # We want to update best_size_for_forbidden[f] for all f subset of complement(mask)
            comp = ((1 << half2) - 1) ^ mask
            # We'll do SOS DP later; for now store candidate
            # Actually we can do: for each f subset of comp, best_size_for_forbidden[f] = max(..., size2[mask])
            # But that's too slow. Instead, we'll do SOS DP on "max size of independent set contained in allowed mask"
            pass

    # Better approach: compute max_indep_size[allowed_mask] = max size of independent set subset of allowed_mask
    max_indep_size = [0] * (1 << half2)
    for mask in range(1 << half2):
        if indep2[mask]:
            max_indep_size[mask] = size2[mask]
    # SOS DP: for each mask, propagate to submasks
    for i in range(half2):
        for mask in range(1 << half2):
            if (mask >> i) & 1:
                max_indep_size[mask] = max(max_indep_size[mask], max_indep_size[mask ^ (1 << i)])

    # Now enumerate independent sets in half1
    # For each, compute forbidden mask in half2
    # Then check if there exists an independent set in half2 of size k - size1 avoiding forbidden
    # That means allowed_mask = complement(forbidden) in half2, need max_indep_size[allowed_mask] >= needed

    # Enumerate all independent sets in half1
    indep1_masks = []
    for mask in range(1 << half1):
        ok = True
        for i in range(half1):
            if (mask >> i) & 1:
                if (adj1[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            indep1_masks.append(mask)

    # Precompute forbidden mask in half2 for each half1 mask
    forbidden_for_mask1 = [0] * (1 << half1)
    for mask in range(1 << half1):
        forb = 0
        for i in range(half1):
            if (mask >> i) & 1:
                # add neighbors in half2
                for j in range(half2):
                    if (adj[v1[i]] >> v2[j]) & 1:
                        forb |= 1 << j
        forbidden_for_mask1[mask] = forb

    for mask1 in indep1_masks:
        s1 = bin(mask1).count("1")
        if s1 > k:
            continue
        need = k - s1
        forb = forbidden_for_mask1[mask1]
        allowed = ((1 << half2) - 1) ^ forb
        if max_indep_size[allowed] >= need:
            # Need to reconstruct an actual set in half2 of size exactly need
            # Find one
            chosen2 = None
            # Search among independent sets subset of allowed
            sub = allowed
            # We'll iterate over submasks of allowed
            submasks = []
            s = sub
            while True:
                if indep2[s] and size2[s] == need:
                    chosen2 = s
                    break
                if s == 0:
                    break
                s = (s - 1) & sub
            if chosen2 is not None:
                # Build answer
                ans = []
                for i in range(half1):
                    if (mask1 >> i) & 1:
                        ans.append(v1[i] + 1)
                for j in range(half2):
                    if (chosen2 >> j) & 1:
                        ans.append(v2[j] + 1)
                print("YES")
                print(" ".join(map(str, ans)))
                return

    print("NO")

if __name__ == "__main__":
    solve()