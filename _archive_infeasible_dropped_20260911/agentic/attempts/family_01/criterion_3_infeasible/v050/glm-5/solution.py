import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    # Iterate a < b < c with a < b, and check if c is in both adj[a] and adj[b].
    # To find lexicographically smallest, iterate a from 1..n, b from a+1..n, c from b+1..n.
    # But that's O(n^3). Instead, for each pair (a,b) that is an edge, intersect their neighbor sets.
    # Since we want lexicographically smallest, iterate a ascending, then b ascending.
    # For each edge (a,b) with a<b, candidates for c are common neighbors > b.
    # Pick the smallest such c.
    # This is O(m * deg) in worst case, but with sets it's O(m * min(deg(a),deg(b))).
    # n<=2000, m<=2e5. Worst case deg ~2000, m*deg could be 4e8, too slow in Python.
    # Better: iterate a from 1 to n. For each a, look at neighbors b>a. For each b, look at neighbors c>b that are also neighbors of a.
    # To speed up, for fixed a, we can iterate b in adj[a] with b>a, and for each b iterate c in adj[b] with c>b and c in adj[a].
    # Use bitsets for fast intersection.
    # Represent adjacency as list of ints (bitsets) for fast & operation.
    # n<=2000, so each bitset fits in 32 Python ints (64-bit each) -> use Python ints as arbitrary precision.
    # Actually Python int can be used as bitset: bit i set means neighbor i.
    # Then adj_bits[a] & adj_bits[b] gives common neighbors. We need smallest c > b.
    # To find smallest c > b in the intersection, we can mask out bits <= b.
    # Let's build adj_bits.
    adj_bits = [0] * (n + 1)
    for u in range(1, n + 1):
        bits = 0
        for v in adj[u]:
            bits |= (1 << v)
        adj_bits[u] = bits
    
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        bits_a = adj_bits[a]
        # neighbors b of a with b > a
        # iterate over adj[a] but only those > a
        # To iterate in ascending order, sort the neighbors > a
        neighbors_a = sorted(v for v in adj[a] if v > a)
        for b in neighbors_a:
            # common neighbors of a and b
            common = bits_a & adj_bits[b]
            # we need c > b
            # mask out bits 0..b
            # create mask with bits > b
            # bits from b+1 to n
            # mask = ~((1 << (b+1)) - 1)
            mask = ~((1 << (b + 1)) - 1)
            common = common & mask
            if common:
                # find lowest set bit
                c = (common & -common).bit_length() - 1
                # c is the smallest common neighbor > b
                # Since we iterate a ascending, b ascending, and pick smallest c, this is lexicographically smallest.
                print(f"{a} {b} {c}")
                return
    
    # Fallback (should not reach due to guarantee)
    # Brute force just in case
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[b]:
                if c <= b:
                    continue
                if c in adj[a]:
                    print(f"{a} {b} {c}")
                    return

solve()