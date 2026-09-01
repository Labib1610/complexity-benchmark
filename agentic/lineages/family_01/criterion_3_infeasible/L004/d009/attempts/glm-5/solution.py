import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges by (u, v) so we process in lexicographic order
    edges.sort()
    
    # For each edge (a, b), we want to find the smallest c > b such that
    # both (a, c) and (b, c) are edges. We iterate c in increasing order.
    # To make this efficient, we use the fact that we process edges in order
    # and can reuse some computation.
    
    # Strategy: for each edge (a, b), iterate c from b+1 to n.
    # Check if c is in both adj[a] and adj[b].
    # To speed up, we can iterate over the smaller of adj[a] and adj[b]
    # (only considering elements > b).
    
    # But we need the smallest c > b. So we can iterate c in order and stop
    # at the first common neighbor > b.
    
    # To make this fast, we can precompute for each vertex its neighbors
    # as a sorted list, and use two pointers or binary search.
    # However, since we need the smallest c > b, we can iterate through
    # the smaller adjacency list and check membership in the other.
    
    # Let's convert adjacency sets to sorted lists for iteration
    adj_list = [sorted(s) for s in adj]
    
    best = None
    
    for a, b in edges:
        # We want smallest c > b with c in adj[a] and c in adj[b]
        # Iterate through the smaller adjacency list
        if len(adj[a]) <= len(adj[b]):
            neighbors = adj_list[a]
            other = adj[b]
        else:
            neighbors = adj_list[b]
            other = adj[a]
        
        # Binary search for first element > b in neighbors
        lo, hi = 0, len(neighbors)
        while lo < hi:
            mid = (lo + hi) // 2
            if neighbors[mid] > b:
                hi = mid
            else:
                lo = mid + 1
        
        for i in range(lo, len(neighbors)):
            c = neighbors[i]
            if c in other:
                # Found a triangle (a, b, c)
                if best is None or (a, b, c) < best:
                    best = (a, b, c)
                break  # smallest c for this edge
    
    # Also need to check: the critically flawed condition is not just triangles.
    # Let me re-read the problem.
    
    # The energy E = x1^2 + 4x2^2 + 9x3^2 - 2x1x2*I12 - 6x2x3*I23 - 3x1x3*I13
    # This is a quadratic form. E = 0 for some non-zero x means the quadratic
    # form is not positive definite, i.e., the matrix is singular or indefinite.
    
    # The matrix is:
    # [1, -I12, -1.5*I13]
    # [-I12, 4, -3*I23]
    # [-1.5*I13, -3*I23, 9]
    
    # Wait, let me be careful. The quadratic form is:
    # E = x1^2 + 4x2^2 + 9x3^2 - 2*I12*x1*x2 - 6*I23*x2*x3 - 3*I13*x1*x3
    # 
    # The symmetric matrix A where E = x^T A x is:
    # A[1,1]=1, A[2,2]=4, A[3,3]=9
    # A[1,2]=A[2,1]=-I12
    # A[2,3]=A[3,2]=-3*I23
    # A[1,3]=A[3,1]=-1.5*I13
    
    # For E=0 with non-zero x, we need det(A)=0 or A indefinite.
    # Since diagonal is positive, if all I's are 0, A is positive definite.
    # 
    # Let's compute det(A) for different cases:
    # det = 1*(4*9 - 9*I23^2) - (-I12)*((-I12)*9 - (-3*I23)*(-1.5*I13)) + (-1.5*I13)*((-I12)*(-3*I23) - 4*(-1.5*I13))
    # = 36 - 9*I23^2 - I12*(9*I12 - 4.5*I23*I13) - 1.5*I13*(3*I12*I23 + 6*I13)
    # = 36 - 9*I23^2 - 9*I12^2 + 4.5*I12*I23*I13 - 4.5*I12*I23*I13 - 9*I13^2
    # = 36 - 9*I12^2 - 9*I23^2 - 9*I13^2
    
    # So det(A) = 9*(4 - I12^2 - I23^2 - I13^2)
    # det = 0 when I12^2 + I23^2 + I13^2 = 4
    # Since each I is 0 or 1, we need exactly 2 of them to be 1 (sum of squares = 2... wait that's not 4)
    # 
    # Hmm, that gives sum = 4, but max is 3. So det is never 0?
    # 
    # Wait, but the problem says critically flawed triplets exist. Let me reconsider.
    # 
    # Actually, for a quadratic form to have E=0 with non-zero x, we don't need det=0.
    # We need the form to be indefinite (has both positive and negative eigenvalues)
    # or semi-definite. If det < 0, then the form is indefinite (since trace > 0,
    # there's at least one positive eigenvalue, and det < 0 means odd number of
    # negative eigenvalues).
    # 
    # det = 9*(4 - I12^2 - I23^2 - I13^2)
    # When all three I's are 1: det = 9*(4-3) = 9 > 0
    # When two I's are 1: det = 9*(4-2) = 18 > 0
    # When one I is 1: det = 9*(4-1) = 27 > 0
    # When zero I's: det = 36 > 0
    # 
    # So det is always positive. But we also need to check if the form is positive
    # semi-definite or indefinite. Since det > 0 and trace > 0, if all leading
    # minors are positive, it's positive definite. If some minor is negative,
    # it could be indefinite.
    # 
    # Leading minors:
    # D1 = 1 > 0
    # D2 = 1*4 - I12^2 = 4 - I12^2
    #   If I12=1: D2 = 3 > 0
    #   If I12=0: D2 = 4 > 0
    # D3 = det = 9*(4 - I12^2 - I23^2 - I13^2) > 0 always
    # 
    # So all leading minors are positive, meaning the form is positive definite
    # for all cases. That means E > 0 for all non-zero x, so no critically flawed
    # triplet exists? But the problem guarantees one exists...
    # 
    # Let me recheck the matrix. The cross terms:
    # -2*x1*x2*I12 contributes -I12 to A[1,2] and A[2,1] (since x1*x2 term in
    # x^T A x is 2*A[1,2]*x1*x2, so 2*A[1,2] = -2*I12, A[1,2] = -I12)
    # -6*x2*x3*I23: 2*A[2,3] = -6*I23, A[2,3] = -3*I23
    # -3*x1*x3*I13: 2*A[1,3] = -3*I13, A[1,3] = -1.5*I13
    # 
    # That's what I had. Let me recompute det more carefully.
    # 
    # A = [[1, -I12, -1.5*I13],
    #      [-I12, 4, -3*I23],
    #      [-1.5*I13, -3*I23, 9]]
    # 
    # det = 1*(4*9 - (-3*I23)*(-3*I23)) - (-I12)*((-I12)*9 - (-3*I23)*(-1.5*I13)) + (-1.5*I13)*((-I12)*(-3*I23) - 4*(-1.5*I13))
    # = 1*(36 - 9*I23^2) + I12*(-9*I12 - 4.5*I23*I13) - 1.5*I13*(3*I12*I23 + 6*I13)
    # = 36 - 9*I23^2 - 9*I12^2 - 4.5*I12*I23*I13 - 4.5*I12*I23*I13 - 9*I13^2
    # = 36 - 9*(I12^2 + I23^2 + I13^2) - 9*I12*I23*I13
    # = 9*(4 - I12^2 - I23^2 - I13^2 - I12*I23*I13)
    # 
    # When all three I's = 1: det = 9*(4 - 1 - 1 - 1 - 1) = 9*0 = 0
    # 
    # So det = 0 when all three edges exist (triangle)!
    # 
    # When exactly 2 edges: det = 9*(4 - 2 - 0) = 18 > 0
    # When exactly 1 edge: det = 9*(4 - 1) = 27 > 0
    # When 0 edges: det = 36 > 0
    # 
    # So critically flawed = triangle (all three edges present).
    # 
    # But wait, we should also check: when det = 0, is the form positive
    # semi-definite (E >= 0 with E=0 possible) or indefinite (E can be < 0)?
    # Either way, E=0 is achievable with non-zero x.
    # 
    # Actually, when det=0, the matrix is singular, so there exists non-zero x
    # with Ax=0, meaning E = x^T A x = x^T (Ax) = 0. So yes, triangle works.
    # 
    # But we should also check if there are other cases where E=0 is possible
    # even with det > 0. If the form is positive definite, E > 0 for all non-zero
    # x, so no. If det > 0 but the form is indefinite... but with all leading
    # minors positive, it's positive definite.
    # 
    # Wait, I need to also check non-leading minors. For positive definiteness,
    # all leading minors must be positive (Sylvester's criterion). We showed
    # D1=1>0, D2=4-I12^2 >= 3 > 0, D3 = det >= 0. 
    # 
    # When all three edges present: D3 = 0, so positive semi-definite (not
    # positive definite). E=0 achievable.
    # When not all three: D3 > 0, D2 > 0, D1 > 0, so positive definite. E > 0
    # for all non-zero x.
    # 
    # So the answer is: find the lexicographically smallest triangle.
    
    if best is not None:
        print(f"{best[0]} {best[1]} {best[2]}")
        return
    
    # Fallback: shouldn't reach here given problem guarantees
    print("1 2 3")

solve()