import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Find all maximal independent sets using Bron-Kerbosch with pivoting.
    mis_list = []
    def bron_kerbosch(R, P, X):
        if P == 0 and X == 0:
            mis_list.append(R)
            return
        # Choose pivot u in P | X with maximum degree in P
        union = P | X
        pivot = -1
        best = -1
        p = union
        while p:
            i = (p & -p).bit_length() - 1
            cnt = bin(adj[i] & P).count('1')
            if cnt > best:
                best = cnt
                pivot = i
            p &= p - 1
        # Candidates = P \ N(pivot)
        if pivot == -1:
            candidates = P
        else:
            candidates = P & ~adj[pivot]
        c = candidates
        while c:
            i = (c & -c).bit_length() - 1
            bit = 1 << i
            bron_kerbosch(R | bit, P & ~adj[i] & ~bit, X & ~adj[i] & ~bit)
            P &= ~bit
            X |= bit
            c &= c - 1

    bron_kerbosch(0, (1 << n) - 1, 0)

    # Sort maximal independent sets by size descending for better pruning.
    mis_list.sort(key=lambda x: bin(x).count('1'), reverse=True)
    k = len(mis_list)

    # Precompute pairwise compatibility: two MIS are compatible iff their intersection is empty.
    compat = [0] * k
    for i in range(k):
        for j in range(i + 1, k):
            if mis_list[i] & mis_list[j] == 0:
                compat[i] |= 1 << j
                compat[j] |= 1 << i

    full = (1 << n) - 1
    color = [-1] * k

    def backtrack(idx, used, count):
        if count == 3:
            return used == full
        if idx >= k:
            return False
        # Prune: even using all remaining largest sets we can't cover the rest.
        rem = full & ~used
        if rem == 0:
            return True
        # Upper bound on coverable vertices from remaining sets.
        coverable = 0
        for j in range(idx, k):
            coverable |= mis_list[j]
        if (coverable & rem) != rem:
            return False
        # Try picking this set.
        if (mis_list[idx] & used) == 0:
            color[idx] = count
            if backtrack(idx + 1, used | mis_list[idx], count + 1):
                return True
            color[idx] = -1
        # Skip this set.
        if backtrack(idx + 1, used, count):
            return True
        return False

    if backtrack(0, 0, 0):
        assignment = [0] * n
        for i in range(k):
            if color[i] != -1:
                s = mis_list[i]
                while s:
                    v = (s & -s).bit_length() - 1
                    assignment[v] = color[i] + 1
                    s &= s - 1
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()