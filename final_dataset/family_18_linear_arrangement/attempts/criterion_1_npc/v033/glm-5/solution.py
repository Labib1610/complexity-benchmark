import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        B = int(next(it))
    except StopIteration:
        return
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u != v:
            adj[u].append(v)
            adj[v].append(u)
    
    # Upper bound: n*(n*n - 1)//3
    THRESHOLD = n * (n*n - 1) // 3
    
    if B >= THRESHOLD:
        # Check if graph is complete and n >= 2
        is_complete = True
        for u in range(n):
            if len(adj[u]) != n - 1:
                is_complete = False
                break
        if is_complete and n >= 2:
            # No solution possible for complete graph
            print("NO")
            return
        # Otherwise, some ordering works; output any permutation
        perm = list(range(1, n+1))
        print("YES")
        print(' '.join(map(str, perm)))
        return
    
    # n <= 30 from constraints implied by bound
    # We can use meet-in-the-middle
    half = n // 2
    n1 = half
    n2 = n - half
    
    # Enumerate all placements for first half
    # For each placement, compute:
    #   a) total cost within first half (for pruning)
    #   b) prefix important counts: for edges into second half, 
    #      count how many neighbors go to each of the n1 positions.
    left_size = 1
    for i in range(1, n1 + 1):
        left_size *= i
    
    candidates = []
    perm1 = list(range(n1))
    import itertools
    for p in itertools.permutations(range(n1)):
        cost_intra = 0
        for i in range(n1):
            pi = p[i]
            for j in adj[i]:
                if j < n1 and i < j:
                    pj = p[j]
                    cost_intra += abs(pi - pj)
        if cost_intra > B:
            continue
        
        # on[j][pos] = number of neighbors of node j (in second half) 
        #              that are placed at position 'pos' in first half
        on = [[0]*n1 for _ in range(n2)]
        for i in range(n1):
            pos = p[i]
            for j in adj[i]:
                if j >= n1:
                    on[j - n1][pos] += 1
        candidates.append((p, on))
    
    if n2 == 0:
        # Only first half exists
        if candidates:
            p, _ = candidates[0]
            bay = [0]*n
            for i in range(n1):
                bay[i] = p[i] + 1
            print("YES")
            print(' '.join(map(str, bay)))
        else:
            print("NO")
        return
    
    # Prepare lookup for second half: rev on counts -> list of positions
    right_size = 1
    for i in range(1, n2 + 1):
        right_size *= i
    
    lookup = {}
    for p2 in itertools.permutations(range(n2)):
        on_rev = [[0]*n2 for _ in range(n1)]
        for j in range(n2):
            pos = p2[j]
            for i in adj[n1 + j]:
                if i < n1:
                    on_rev[i][pos] += 1
        key = tuple(tuple(row) for row in on_rev)
        if key not in lookup:
            lookup[key] = p2
            if len(lookup) == right_size:
                break
    
    # Search for match
    for p, on in candidates:
        key = tuple(tuple(row) for row in on)
        if key in lookup:
            p2 = lookup[key]
            # Compute total cost
            total_cost = 0
            # within first half
            for i in range(n1):
                pi = p[i]
                for j in adj[i]:
                    if j < n1 and i < j:
                        total_cost += abs(pi - p[j])
            # within second half
            for j_local in range(n2):
                j = n1 + j_local
                pj = p2[j_local]
                for k in adj[j]:
                    if n1 <= k < j:
                        k_local = k - n1
                        total_cost += abs(pj - p2[k_local])
            # between halves
            for i in range(n1):
                pi = p[i]
                for j in adj[i]:
                    if j >= n1:
                        j_local = j - n1
                        total_cost += abs(pi - p2[j_local])
            
            if total_cost <= B:
                bay = [0]*n
                for i in range(n1):
                    bay[i] = p[i] + 1
                for j in range(n2):
                    bay[n1 + j] = p2[j] + 1
                print("YES")
                print(' '.join(map(str, bay)))
                return
    
    # Fallback: brute force for n <= 8
    if n <= 8:
        for perm in itertools.permutations(range(n)):
            cost = 0
            for u in range(n):
                pu = perm[u]
                for v in adj[u]:
                    if u < v:
                        cost += abs(pu - perm[v])
            if cost <= B:
                result = [x+1 for x in perm]
                print("YES")
                print(' '.join(map(str, result)))
                return
    
    print("NO")

solve()