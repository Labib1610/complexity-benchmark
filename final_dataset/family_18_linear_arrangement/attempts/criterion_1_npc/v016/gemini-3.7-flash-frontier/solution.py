import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    adj = [0] * n
    deg = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        deg[u] += 1
        deg[v] += 1

    size = 1 << n
    cut = [0] * size
    dp = [10**15] * size
    parent = [0] * size

    dp[0] = 0

    # Precompute lowest set bit index and bit value for fast iteration
    for mask in range(1, size):
        lsb = mask & -mask
        v = (lsb).bit_length() - 1
        prev = mask ^ lsb
        
        # cut[mask] = cut[prev] + deg[v] - 2 * (edges from v to prev)
        cut[mask] = cut[prev] + deg[v] - 2 * (adj[v] & prev).bit_count()
        
        # Find best predecessor
        # Iterate over all set bits in mask
        temp = mask
        min_cost = 10**15
        best_u = -1
        while temp:
            b = temp & -temp
            u = b.bit_length() - 1
            cost = dp[mask ^ b]
            if cost < min_cost:
                min_cost = cost
                best_u = u
            temp ^= b
            
        dp[mask] = min_cost + (cut[mask] if mask != size - 1 else 0)
        parent[mask] = best_u

    if dp[size - 1] <= B:
        print("YES")
        # Reconstruct the order of vertices
        order = []
        curr = size - 1
        while curr > 0:
            u = parent[curr]
            order.append(u)
            curr ^= (1 << u)
        order.reverse()
        
        # order[i] is placed at position i + 1
        pos = [0] * n
        for p, u in enumerate(order):
            pos[u] = p + 1
        print(*(pos[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()