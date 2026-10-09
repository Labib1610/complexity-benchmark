import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    if n == 0:
        return
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
        if u != v:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)

    for i in range(n):
        deg[i] = bin(adj[i]).count('1')

    num_states = 1 << n
    cut = [0] * num_states
    dp = [float('inf')] * num_states
    dp[0] = 0

    for mask in range(1, num_states):
        # Lowest set bit
        low_bit = mask & -mask
        v = (low_bit).bit_length() - 1
        prev = mask ^ low_bit
        cut[mask] = cut[prev] + deg[v] - 2 * bin(adj[v] & prev).count('1')
        
        # Transition
        min_prev = float('inf')
        temp = mask
        while temp > 0:
            b = temp & -temp
            p = mask ^ b
            if dp[p] < min_prev:
                min_prev = dp[p]
            temp ^= b
            
        dp[mask] = min_prev + cut[mask]

    min_cost = dp[num_states - 1]
    if min_cost > B:
        print("NO")
        return

    print("YES")
    # Reconstruct order
    order = [0] * n
    curr = num_states - 1
    for pos in range(n, 0, -1):
        temp = curr
        while temp > 0:
            b = temp & -temp
            u = b.bit_length() - 1
            prev = curr ^ b
            if dp[curr] == dp[prev] + cut[curr]:
                order[u] = pos
                curr = prev
                break
            temp ^= b

    print(*(order[i] for i in range(n)))

if __name__ == '__main__':
    solve()