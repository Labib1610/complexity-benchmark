import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    full = (1 << (n + 1)) - 1
    # Precompute independent sets via DP over subsets
    ind = [False] * (1 << (n + 1))
    ind[0] = True
    for mask in range(1, 1 << (n + 1)):
        low = mask & (-mask)
        v = low.bit_length() - 1
        prev = mask ^ low
        if ind[prev] and (adj[v] & prev) == 0:
            ind[mask] = True
    
    # Collect maximal independent sets (only those not subset of another)
    maximal = []
    for mask in range(1 << (n + 1)):
        if ind[mask]:
            # Check if mask is maximal: adding any vertex outside creates conflict
            is_max = True
            outside = full ^ mask
            temp = outside
            while temp:
                low = temp & (-temp)
                v = low.bit_length() - 1
                if (adj[v] & mask) == 0:
                    is_max = False
                    break
                temp ^= low
            if is_max:
                maximal.append(mask)
    
    # Try to cover all vertices with 3 independent sets
    for a in maximal:
        rem1 = full ^ a
        if rem1 == 0:
            # Assign all to shift 1
            res = [1] * (n + 1)
            print("YES")
            print(" ".join(str(res[i]) for i in range(1, n + 1)))
            return
        for b in maximal:
            if (b & rem1) == b:
                rem2 = rem1 ^ b
                if rem2 == 0:
                    res = [0] * (n + 1)
                    for i in range(1, n + 1):
                        if (a >> i) & 1:
                            res[i] = 1
                        elif (b >> i) & 1:
                            res[i] = 2
                    print("YES")
                    print(" ".join(str(res[i]) for i in range(1, n + 1)))
                    return
                # rem2 must be independent (subset of some maximal)
                # Check if rem2 is independent
                if ind[rem2]:
                    res = [0] * (n + 1)
                    for i in range(1, n + 1):
                        if (a >> i) & 1:
                            res[i] = 1
                        elif (b >> i) & 1:
                            res[i] = 2
                        else:
                            res[i] = 3
                    print("YES")
                    print(" ".join(str(res[i]) for i in range(1, n + 1)))
                    return
    
    print("NO")

solve()