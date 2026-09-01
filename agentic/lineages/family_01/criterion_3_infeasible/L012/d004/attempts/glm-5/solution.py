import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (3-clique) in the graph.
    # A triangle is exactly a group of three sensors where all three pairs share an interlock.
    # If all three pairs share an interlock, then no matter how we assign two bands,
    # by pigeonhole principle at least two of the three must be in the same band,
    # and since they share an interlock, this is a contradiction.
    # The problem guarantees at least one such triangle exists.
    # We need the lexicographically smallest triangle (a, b, c) with a < b < c.
    
    # To find the lexicographically smallest triangle:
    # Iterate a from 1 to n.
    # For each a, iterate b from a+1 to n such that (a,b) is an edge.
    # For each such b, iterate c from b+1 to n such that (a,c) and (b,c) are edges.
    # The first found triangle is the lexicographically smallest.
    # But this can be O(n^3) in worst case if done naively.
    
    # Optimization: For each a, we look at its neighbors. We want to find two neighbors b, c of a
    # with b < c, (b,c) is an edge, and we want the smallest b, then smallest c.
    # So for fixed a, iterate b over sorted neighbors of a that are > a.
    # For each b, iterate c over sorted neighbors of a that are > b, and check if (b,c) is an edge.
    # To make checking (b,c) fast, we can use the adjacency sets.
    # But iterating all pairs of neighbors could be O(sum of deg(a)^2) which might be large.
    
    # Better approach: For each a, iterate b over neighbors of a with b > a.
    # For each b, iterate c over neighbors of b with c > b, and check if c is in adj[a].
    # To get lexicographically smallest, we need to be careful.
    # Actually, we want smallest a, then smallest b, then smallest c.
    # So for a from 1 to n:
    #   neighbors_a = sorted list of neighbors of a that are > a
    #   for b in neighbors_a:
    #       for c in neighbors_a:
    #           if c > b and c in adj[b]:
    #               return (a, b, c)
    # But this is O(sum deg(a)^2) which could be up to O(n * m) in dense graphs? 
    # Actually sum of deg(a)^2 can be large. For n=2000, m=2e5, average degree ~200, sum deg^2 ~ 2000*200^2 = 8e7, might be okay in Python? Maybe borderline.
    
    # Alternative: For each a, we can iterate b in neighbors of a (b > a), and for each b, iterate c in neighbors of b (c > b), and check if c in adj[a] and c > a.
    # But to ensure lexicographic order, we need to find the smallest b first.
    # So for fixed a, we iterate b in sorted neighbors of a (b > a). For each b, we iterate c in sorted neighbors of b (c > b), and check if c in adj[a]. The first such c gives the smallest c for this b. And since we iterate b in increasing order, the first found (b,c) gives the lexicographically smallest for this a.
    # This is O(sum over a of sum over b in N(a) of deg(b)). In worst case, this could be O(n * m) = 2000 * 2e5 = 4e8, too slow.
    
    # We need a more efficient method. 
    # Since we want the lexicographically smallest triangle, we can try to find it by checking for each a, whether there exists a triangle containing a as the smallest vertex.
    # For a fixed a, we want to find b, c > a such that (a,b), (a,c), (b,c) are edges, with b < c minimal.
    # This is equivalent to finding an edge (b,c) in the subgraph induced by neighbors of a, with b, c > a, and b < c minimal.
    # To find the lexicographically smallest such (b,c), we can iterate b from a+1 to n, and for each b that is a neighbor of a, we check if there exists c > b that is a neighbor of both a and b.
    # So for fixed a, for b from a+1 to n:
    #   if b in adj[a]:
    #       for c from b+1 to n:
    #           if c in adj[a] and c in adj[b]:
    #               return (a, b, c)
    # This is O(n^3) in worst case, too slow.
    
    # We need a better approach. Let's think about the degree ordering.
    # A common trick for triangle listing: orient edges from lower degree to higher degree (or lower index to higher index if degrees equal). Then each vertex has out-degree at most O(sqrt(m)). Then for each vertex, we can mark its out-neighbors, and for each out-neighbor, check its out-neighbors.
    # But we need lexicographically smallest triangle, which complicates things.
    
    # Let's think differently. We want the lexicographically smallest triangle (a,b,c).
    # We can iterate a from 1 to n. For each a, we want to know if there's a triangle with smallest vertex a.
    # For a fixed a, we consider the subgraph induced by neighbors of a that are > a. We want the lexicographically smallest edge (b,c) in this subgraph with b < c.
    # To find this, we can iterate b from a+1 to n. If b is a neighbor of a, we then iterate c from b+1 to n. If c is a neighbor of a and a neighbor of b, we found it.
    # But this is O(n^3). We need to speed up the inner check.
    
    # For a fixed a, let S = sorted list of neighbors of a that are > a.
    # We want to find b, c in S with b < c and (b,c) is an edge, minimizing b then c.
    # We can iterate b in S in increasing order. For each b, we want the smallest c in S with c > b and (b,c) is an edge.
    # To find this quickly, we can iterate c in S with c > b, and check if c in adj[b]. But this is O(|S|^2) per a.
    # Sum of |S|^2 over all a could be large.
    
    # Alternative: For each a, we can iterate b in S. For each b, we iterate over neighbors of b that are > b, and check if they are in S. To make this efficient, we can represent S as a boolean array or a set.
    # But iterating over neighbors of b could be O(deg(b)) per b, and sum over b in S of deg(b) could be large.
    
    # Let's consider the degree ordering approach for triangle listing, but adapted for lexicographic order.
    # Actually, since we only need the first triangle in lexicographic order, we can use the following:
    # For a from 1 to n:
    #   For b from a+1 to n:
    #     if (a,b) is edge:
    #       For c from b+1 to n:
    #         if (a,c) is edge and (b,c) is edge:
    #           return (a,b,c)
    # This is O(n^3) but with early termination. In the worst case where the lexicographically smallest triangle is near the end, it's slow.
    
    # We need a more efficient way. Let's think about the structure.
    # The lexicographically smallest triangle has the smallest possible a. So we can first find the smallest a that is part of any triangle.
    # For a given a, we want to know if there exist b, c > a such that (a,b), (a,c), (b,c) are edges.
    # This is equivalent to: in the subgraph induced by neighbors of a, is there an edge between two vertices both > a?
    # To check this, we can iterate over edges (b,c) where b, c > a and both are neighbors of a.
    # But how to do this efficiently for each a?
    
    # Another idea: For each edge (b,c) with b < c, we can check if there exists a < b such that a is connected to both b and c. The smallest such a for this edge gives a triangle (a,b,c). We want the lexicographically smallest triangle, so we want the smallest a, then smallest b, then smallest c.
    # So we can iterate a from 1 to n. For each a, we look at all edges (b,c) where b, c > a and both are neighbors of a. We want the one with smallest b, then smallest c.
    # To do this, for each a, we can iterate b in neighbors of a with b > a, in increasing order. For each b, we iterate c in neighbors of a with c > b, in increasing order, and check if (b,c) is an edge. The first found is the answer.
    # This is O(sum over a of |N(a) > a|^2). In the worst case, if the graph is dense, this is O(n * (n)^2) = O(n^3), too slow.
    
    # We need a better approach. Let's think about the following:
    # For each vertex a, we want to find the smallest b > a such that b is a neighbor of a, and there exists c > b such that c is a neighbor of both a and b.
    # For a fixed a and b, we want the smallest c > b such that c is in adj[a] and adj[b].
    # So we can iterate a from 1 to n. For each a, we iterate b from a+1 to n. If b in adj[a], we then want the smallest c > b such that c in adj[a] and c in adj[b].
    # To find this c quickly, we can precompute for each pair (a,b) the smallest common neighbor > b. But that's too much memory.
    
    # Alternative: For each a, we can iterate b in adj[a] with b > a, in increasing order. For each b, we iterate c in adj[b] with c > b, in increasing order, and check if c in adj[a]. The first such c gives the answer for this a. Since we iterate b in increasing order, and for each b we iterate c in increasing order, the first found (b,c) is the lexicographically smallest for this a.
    # The complexity is O(sum over a of sum over b in N(a), b>a of deg(b)). In the worst case, this is O(n * m) = 4e8, too slow for Python.
    
    # We need to optimize. Notice that we only need the first triangle. So we can stop early.
    # Also, we can use the fact that we want the lexicographically smallest, so we can try to find it by checking smaller a first.
    # For a given a, we can check if there's any triangle with smallest vertex a. If yes, we find the smallest b and c. If not, we move to a+1.
    # To check if there's a triangle with smallest vertex a, we can use the following:
    # Let S = {v in adj[a] | v > a}. We want to know if there's an edge in the subgraph induced by S.
    # We can iterate over edges (u,v) in the original graph where u, v in S. But how to do this efficiently?
    # We can iterate over all edges (u,v) with u < v. For each edge, if u > a and v > a and u in adj[a] and v in adj[a], then (a,u,v) is a triangle. But we want the smallest a, so we'd need to process edges in a way that finds the smallest a first.
    
    # Another idea: For each edge (b,c) with b < c, the smallest a that forms a triangle with this edge is the smallest common neighbor of b and c that is < b. So we can iterate over edges (b,c) in lexicographic order, and for each edge, find the smallest common neighbor a < b. The first edge that has such an a gives the lexicographically smallest triangle? Not necessarily, because we need the smallest a first, then smallest b, then smallest c. So we should iterate a from 1 to n, and for each a, find the smallest b, then smallest c.
    
    # Let's think about the following approach:
    # For each a from 1 to n:
    #   Let S = sorted list of neighbors of a that are > a.
    #   We want to find the smallest b in S such that there exists c in S with c > b and (b,c) is an edge.
    #   To do this, we can iterate b in S in increasing order. For each b, we want to know if there's any c in S with c > b and (b,c) is an edge.
    #   To check this, we can iterate over neighbors of b that are > b, and see if any of them are in S.
    #   But to make it efficient, we can mark the elements of S in a boolean array (or a set), and then for each b in S, iterate over neighbors of b that are > b, and check if they are in S.
    #   The first b that has such a neighbor gives us the smallest b. Then we need the smallest c > b in S that is a neighbor of b.
    #   So for that b, we iterate over neighbors of b that are > b, in increasing order, and check if they are in S. The first one is the smallest c.
    #   This gives us the lexicographically smallest triangle for this a.
    #   If no such b exists, we move to a+1.
    # The complexity for a given a is O(|S| + sum over b in S of deg(b)). In the worst case, this is O(n + m) per a, so O(n*(n+m)) total, which is too slow.
    
    # We need a more efficient method. Let's think about the degree ordering trick.
    # Orient each edge from lower degree to higher degree (break ties by index). Then each vertex has out-degree at most O(sqrt(m)). 
    # For each vertex a, we can look at its out-neighbors and in-neighbors. But we need lexicographic order.
    # Actually, since we want the lexicographically smallest triangle, we can use the following:
    # For each a from 1 to n:
    #   For each b in adj[a] with b > a:
    #     For each c in adj[b] with c > b:
    #       if c in adj[a]:
    #         return (a, b, c)
    # But this is O(sum over a of sum over b in N(a) of deg(b)), which is O(n*m) in worst case.
    
    # We need to optimize the inner loop. Notice that for fixed a and b, we want to find if there's any c > b such that c is in both adj[a] and adj[b]. 
    # We can precompute for each a a sorted list of its neighbors. Then for fixed a and b, we can find the intersection of adj[a] and adj[b] for elements > b.
    # But computing intersection of two sets takes O(min(|adj[a]|, |adj[b]|)) time if we iterate over the smaller set.
    # So for fixed a, we can iterate b in adj[a] with b > a. For each b, we iterate over the smaller of adj[a] and adj[b] (restricted to > b), and check if the element is in the other set.
    # This is O(sum over a of sum over b in N(a) of min(deg(a), deg(b))).
    # In the worst case, this is still O(n * m), but in practice it might be faster.
    
    # Given the constraints (n=2000, m=2e5), and time limit 2s, we need something that works in Python.
    # Let's try the following approach:
    # For each a from 1 to n:
    #   S = sorted list of neighbors of a that are > a
    #   if len(S) < 2: continue
    #   We want to find b, c in S with b < c and (b,c) is an edge, minimizing b then c.
    #   We can iterate b in S in increasing order. For each b, we want the smallest c in S with c > b and (b,c) is an edge.
    #   To find this, we can iterate over neighbors of b that are > b, in increasing order, and check if they are in S.
    #   To make the check fast, we can represent S as a set.
    #   So for each b in S:
    #     for c in sorted(adj[b]):
    #       if c > b and c in S_set:
    #         return (a, b, c)
    #   But sorting adj[b] for each b is expensive. Instead, we can iterate over adj[b] and collect those > b, then sort them. But that's also expensive.
    #   Alternatively, we can pre-sort the adjacency lists.
    
    # Let's pre-sort the adjacency lists. Then for each a, S = [v for v in adj[a] if v > a] (already sorted if adj[a] is sorted).
    # S_set = set(S)
    # for b in S:
    #   for c in adj[b]:
    #     if c > b and c in S_set:
    #       return (a, b, c)
    # This is O(sum over a of sum over b in S of deg(b)). In worst case, O(n*m).
    # But with early termination, it might be fast enough if the answer is found early.
    # However, the problem says the answer is guaranteed to exist, but it could be anywhere.
    
    # We need a better worst-case bound. Let's think about the following:
    # For each edge (b,c) with b < c, we can find the smallest a < b such that a is connected to both b and c. This gives a triangle (a,b,c). We want the lexicographically smallest such triangle.
    # So we can iterate over all edges (b,c) in lexicographic order (sorted by b, then c). For each edge, we find the smallest common neighbor a < b. The first edge that has such an a gives the lexicographically smallest triangle? Not necessarily, because we need the smallest a first. So we should iterate a from 1 to n, and for each a, find the smallest b, then smallest c.
    
    # Another idea: For each a, we can find the smallest b > a such that b is in adj[a] and there exists c > b with c in adj[a] and adj[b]. 
    # To find this b, we can iterate b from a+1 to n. If b in adj[a], we check if adj[a] and adj[b] have a common element > b. 
    # To check this quickly, we can iterate over the smaller of adj[a] and adj[b] (restricted to > b), and check if the element is in the other set.
    # So for fixed a, for b from a+1 to n:
    #   if b in adj[a]:
    #     # find if there exists c > b with c in adj[a] and c in adj[b]
    #     # iterate over the smaller set
    #     if len(adj[a]) <= len(adj[b]):
    #       for c in adj[a]:
    #         if c > b and c in adj[b]:
    #           return (a, b, c)
    #     else:
    #       for c in adj[b]:
    #         if c > b and c in adj[a]:
    #           return (a, b, c)
    # This is O(sum over a of sum over b in N(a) of min(deg(a), deg(b))).
    # In the worst case, this is O(n * m), but with the min, it might be better in practice.
    # For n=2000, m=2e5, average degree 200, so min(deg(a), deg(b)) is at most 200, and sum over b in N(a) is 200, so per a it's 200*200=4e4, total 2000*4e4=8e7, which might be okay in Python with early termination.
    
    # Let's implement this. We'll precompute adjacency lists as sets for fast membership testing.
    # We'll also keep them as sorted lists for iteration, but actually we can just iterate over the set.
    # To optimize, we can convert adj[a] to a sorted list once, but for membership we use the set.
    
    adj_set = [set() for _ in range(n + 1)]
    adj_list = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj_set[u].add(v)
        adj_set[v].add(u)
        adj_list[u].append(v)
        adj_list[v].append(u)
    for i in range(1, n + 1):
        adj_list[i].sort()
    
    for a in range(1, n + 1):
        # We want to find b > a, c > b such that (a,b), (a,c), (b,c) are edges.
        # Iterate b from a+1 to n.
        for b in adj_list[a]:
            if b <= a:
                continue
            # Now we want c > b such that c in adj_set[a] and c in adj_set[b].
            # Iterate over the smaller of adj_set[a] and adj_set[b] (restricted to > b).
            # To make it efficient, we can iterate over adj_list[a] or adj_list[b] and check membership.
            # But we need c > b. Since adj_list is sorted, we can binary search for the first element > b, but that's extra work.
            # Instead, we can just iterate and skip elements <= b.
            if len(adj_set[a]) <= len(adj_set[b]):
                for c in adj_list[a]:
                    if c > b and c in adj_set[b]:
                        print(a, b, c)
                        return
            else:
                for c in adj_list[b]:
                    if c > b and c in adj_set[a]:
                        print(a, b, c)
                        return

solve()