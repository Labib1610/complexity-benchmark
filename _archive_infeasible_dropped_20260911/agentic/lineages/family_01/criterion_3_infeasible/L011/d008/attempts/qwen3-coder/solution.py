import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # We'll store for each sequence, which positions it has a 1 in
    # But since m can be up to 200000, we can't store sets of positions
    # Instead, we'll store for each pair (i,j) how many times they are together
    
    # Let's think differently:
    # For each operation k, we have a pair (u,v). 
    # After all operations, W(S_i) = degree of node i in the graph formed by operations
    # d(S_i, S_j) = W(S_i) + W(S_j) - 2 * (number of positions where both are 1)
    # But both S_i and S_j are 1 exactly when both were chosen in the same operation
    # So d(S_i, S_j) = W(S_i) + W(S_j) - 2 * count_of_times_both_i_j_appear_together
    
    # Let's count how many times each pair appears together
    pair_count = defaultdict(int)
    degrees = [0] * (n + 1)
    
    idx = 2
    operations = []
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        operations.append((u, v))
        pair_count[(u, v)] += 1
        degrees[u] += 1
        degrees[v] += 1
    
    # Now for any triplet (a,b,c), we want:
    # d(a,b) + d(b,c) + d(c,a) = 2*(W(a) + W(b) + W(c)) - 6
    # Where d(i,j) = degrees[i] + degrees[j] - 2*pair_count[(i,j)] (if i<j)
    
    # So: 
    # (degrees[a]+degrees[b]-2*Cab) + (degrees[b]+degrees[c]-2*Cbc) + (degrees[c]+degrees[a]-2*Cac) 
    # = 2*(degrees[a] + degrees[b] + degrees[c]) - 6
    # Simplifying:
    # 2*(degrees[a] + degrees[b] + degrees[c]) - 2*(Cab + Cbc + Cac) 
    # = 2*(degrees[a] + degrees[b] + degrees[c]) - 6
    # Which gives:
    # -2*(Cab + Cbc + Cac) = -6
    # So: Cab + Cbc + Cac = 3
    
    # Since each Cxy is the count of how many times pair (x,y) appears, and each operation contributes 1,
    # and all operations have distinct pairs, each Cxy is either 0 or 1.
    # So we need exactly 3 pairs among {{a,b}, {b,c}, {a,c}} to appear in the operations.
    # But since all operations have distinct pairs, and each Cxy is 0 or 1, 
    # we need exactly 3 of the 3 possible pairs {a,b}, {b,c}, {a,c} to exist in the operation list.
    
    # That means, we're looking for a triangle in the graph formed by the operations.
    # And among all triangles, we want the lexicographically smallest one.
    
    # Build adjacency info
    adj = [set() for _ in range(n + 1)]
    edge_exists = set()
    
    for u, v in operations:
        adj[u].add(v)
        adj[v].add(u)
        edge_exists.add((u, v))
    
    # Find the lexicographically smallest triangle
    for a in range(1, n + 1):
        neighbors = sorted(list(adj[a]))
        # Check all pairs of neighbors of a
        for i in range(len(neighbors)):
            b = neighbors[i]
            if b <= a:
                continue
            for j in range(i + 1, len(neighbors)):
                c = neighbors[j]
                if c <= b:
                    continue
                # Check if edge b-c exists
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()