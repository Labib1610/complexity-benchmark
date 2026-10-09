import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Find all maximal cliques (Bron-Kerbosch with pivoting)
    cliques = []

    def bron_kerbosch(R, P, X):
        if P == 0 and X == 0:
            cliques.append(R)
            return
        # Choose pivot to minimize branches
        pivot = -1
        best = -1
        combined = P | X
        while combined:
            v_bit = combined & -combined
            v = v_bit.bit_length() - 1
            cnt = bin(adj[v] & P).count('1')
            if cnt > best:
                best = cnt
                pivot = v
            combined ^= v_bit
        # Candidates: P \ N(pivot)
        candidates = P & ~adj[pivot]
        while candidates:
            v_bit = candidates & -candidates
            v = v_bit.bit_length() - 1
            newP = P & adj[v]
            newX = X & adj[v]
            bron_kerbosch(R | (1 << v), newP, newX)
            P ^= v_bit
            X |= v_bit
            candidates ^= v_bit

    bron_kerbosch(0, (1 << n) - 1, 0)

    # Check if any clique has size > 3
    for c in cliques:
        if bin(c).count('1') > 3:
            print("NO")
            return

    # 3-coloring using backtracking with clique-based pruning
    color = [0] * n

    def backtrack(pos):
        if pos == n:
            return True
        used = 0
        for j in range(pos):
            if adj[pos] & (1 << j):
                used |= 1 << color[j]
        for c in range(3):
            if not (used & (1 << c)):
                color[pos] = c
                if backtrack(pos + 1):
                    return True
        color[pos] = 0
        return False

    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

solve()