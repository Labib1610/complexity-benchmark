import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    triples = []
    idx = 2
    for _ in range(t):
        m = int(data[idx]); p = int(data[idx+1]); s = int(data[idx+2])
        idx += 3
        triples.append((m-1, p-1, s-1))
    
    # Build bipartite graph between p and s, with edge labels being m.
    # We need a perfect matching of size k, and the matched m's must be a permutation of 0..k-1.
    adj = [[] for _ in range(k)]
    edge_m = {}
    for m, p, s in triples:
        adj[p].append(s)
        edge_m[(p, s)] = m
    
    # Try all permutations of m assignment to p positions (i.e., organism for membrane m uses pathway perm[m]).
    # Then check if s can be matched.
    # But k up to 22, too large for permutations.
    # Instead, use backtracking with matching, trying to assign organisms.
    
    # We'll do backtracking over membranes 0..k-1, each membrane picks a (p,s) edge.
    # Maintain used_p, used_s bitmasks.
    # To speed up, precompute edges grouped by m.
    edges_by_m = [[] for _ in range(k)]
    for m, p, s in triples:
        edges_by_m[m].append((p, s))
    
    # Sort edges_by_m by length for better pruning
    order = sorted(range(k), key=lambda x: len(edges_by_m[x]))
    
    assignment = [None] * k  # assignment[m] = (p, s)
    used_p = 0
    used_s = 0
    
    # Hopcroft-Karp-like augmenting matching won't directly work because of the m constraint.
    # Use DFS with pruning.
    
    def backtrack(i, used_p, used_s):
        if i == k:
            return True
        m = order[i]
        for (p, s) in edges_by_m[m]:
            if not (used_p >> p) & 1 and not (used_s >> s) & 1:
                assignment[m] = (p, s)
                if backtrack(i+1, used_p | (1 << p), used_s | (1 << s)):
                    return True
        return False
    
    if backtrack(0, 0, 0):
        out = ["YES"]
        for m in range(k):
            p, s = assignment[m]
            out.append(f"{m+1} {p+1} {s+1}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()