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
    
    half = n // 2
    A = list(range(half))
    B = list(range(half, n))
    A_mask = (1 << half) - 1
    B_mask = ((1 << (n - half)) - 1) << half
    
    # Adjacency within B (using B-local indices)
    adjB = [0] * len(B)
    for i, v in enumerate(B):
        for j, u in enumerate(B):
            if v != u and (adj[v] >> u) & 1:
                adjB[i] |= (1 << j)
    
    # Cross adjacency: for each vertex in A, which B-vertices are forbidden
    cross = [0] * len(A)
    for i, v in enumerate(A):
        for j, u in enumerate(B):
            if (adj[v] >> u) & 1:
                cross[i] |= (1 << j)
    
    # Enumerate independent sets of A
    indA = []
    for mask in range(1 << len(A)):
        ok = True
        temp = mask
        while temp:
            v = (temp & -temp).bit_length() - 1
            if mask & adj[v] & A_mask:
                ok = False
                break
            temp &= temp - 1
        if ok:
            indA.append(mask)
    
    # Precompute maxIS for all subsets of B
    sizeB = len(B)
    maxIS = [0] * (1 << sizeB)
    for T in range(1, 1 << sizeB):
        v = (T & -T).bit_length() - 1
        without_v = T & ~(1 << v)
        val = maxIS[without_v]
        remaining = T & ~adjB[v] & ~(1 << v)
        val2 = 1 + maxIS[remaining]
        maxIS[T] = max(val, val2)
    
    # Find solution
    for maskA in indA:
        s = bin(maskA).count('1')
        if s > k:
            continue
        need = k - s
        forbidden = 0
        temp = maskA
        while temp:
            v = (temp & -temp).bit_length() - 1
            forbidden |= cross[v]
            temp &= temp - 1
        valid = ((1 << sizeB) - 1) & ~forbidden
        if maxIS[valid] >= need:
            # Reconstruct independent set in B of size 'need' within 'valid'
            chosenB = 0
            remaining_valid = valid
            remaining_need = need
            for v in range(sizeB):
                if remaining_need == 0:
                    break
                if (remaining_valid >> v) & 1:
                    # Try including v
                    new_valid = remaining_valid & ~adjB[v] & ~(1 << v)
                    if maxIS[new_valid] >= remaining_need - 1:
                        chosenB |= (1 << v)
                        remaining_valid = new_valid
                        remaining_need -= 1
            # Build result
            result = []
            for i in range(len(A)):
                if (maskA >> i) & 1:
                    result.append(A[i] + 1)
            for j in range(sizeB):
                if (chosenB >> j) & 1:
                    result.append(B[j] + 1)
            print("YES")
            print(' '.join(map(str, result)))
            return
    
    print("NO")

solve()