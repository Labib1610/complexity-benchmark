import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    adj = [0] * n
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    if k == 0:
        print("YES")
        print()
        return
    
    half = n // 2
    left_size = half
    right_size = n - half
    
    left_mask = (1 << left_size) - 1
    
    def enumerate_independent_sets(vertices, adj):
        sets = []
        n_v = len(vertices)
        local_adj = [0] * n_v
        for i, v in enumerate(vertices):
            for j, u in enumerate(vertices):
                if adj[v] & (1 << u):
                    local_adj[i] |= (1 << j)
        
        def backtrack(idx, current, forbidden):
            if idx == n_v:
                sets.append(current)
                return
            # Don't include vertex idx
            backtrack(idx + 1, current, forbidden)
            # Include vertex idx if not forbidden
            if not (forbidden & (1 << idx)):
                backtrack(idx + 1, current | (1 << idx), forbidden | local_adj[idx])
        
        backtrack(0, 0, 0)
        return sets
    
    left_vertices = list(range(left_size))
    right_vertices = list(range(left_size, n))
    
    left_sets = enumerate_independent_sets(left_vertices, adj)
    right_sets = enumerate_independent_sets(right_vertices, adj)
    
    # For right sets, group by size
    right_by_size = {}
    for s in right_sets:
        sz = bin(s).count('1')
        if sz not in right_by_size:
            right_by_size[sz] = s
    
    # For each left set, find right set that completes to k
    for ls in left_sets:
        ls_size = bin(ls).count('1')
        if ls_size > k:
            continue
        need = k - ls_size
        if need in right_by_size:
            rs = right_by_size[need]
            # Verify no edges between left and right selections
            # Left set vertices
            left_verts = [i for i in range(left_size) if ls & (1 << i)]
            right_verts = [i + left_size for i in range(right_size) if rs & (1 << i)]
            
            valid = True
            for lv in left_verts:
                for rv in right_verts:
                    if adj[lv] & (1 << rv):
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                result = left_verts + right_verts
                result.sort()
                print("YES")
                print(' '.join(str(x + 1) for x in result))
                return
    
    print("NO")

solve()