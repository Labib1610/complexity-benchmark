import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    if n == 0:
        print("YES")
        print()
        return

    adj = [0] * n
    deg = [0] * n
    
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            deg[u] += 1
            deg[v] += 1

    size = 1 << n
    dp = [0] * size
    cut = [0] * size
    parent = [0] * size
    
    for mask in range(1, size):
        lsb = mask & -mask
        u = lsb.bit_length() - 1
        prev = mask ^ lsb
        cut[mask] = cut[prev] + deg[u] - 2 * (adj[u] & prev).bit_count()
        
        if prev == 0:
            dp[mask] = 0
            parent[mask] = u
        else:
            min_val = 10**18
            best_v = -1
            temp = mask
            while temp:
                v_lsb = temp & -temp
                v = v_lsb.bit_length() - 1
                p = mask ^ v_lsb
                val = dp[p] + cut[p]
                if val < min_val:
                    min_val = val
                    best_v = v
                temp ^= v_lsb
            dp[mask] = min_val
            parent[mask] = best_v

    total_cost = dp[size - 1]
    if total_cost > B:
        print("NO")
    else:
        print("YES")
        order = []
        curr = size - 1
        while curr > 0:
            v = parent[curr]
            order.append(v)
            curr ^= (1 << v)
        order.reverse()
        
        pos = [0] * n
        for bay, mod in enumerate(order, 1):
            pos[mod] = bay
        print(*(pos[i] for i in range(n)))

if __name__ == '__main__':
    solve()