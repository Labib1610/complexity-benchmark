import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    # Precompute valid pairs for (s_u, s_v) in {1, 2, 3}^2
    valid_pair = [[False] * 4 for _ in range(4)]
    for su in range(1, 4):
        for sv in range(1, 4):
            # Matrix:
            # su, sv, su^2 + u + v + 10
            # 1,  1,  sv
            # sv, su, su*sv
            # Determinant = su*(sv - su*sv) - sv*(su*sv - sv) + (su^2 + u + v + 10)*(su - sv)
            # = su*sv*(1 - su) - sv^2*(su - 1) + (su^2 + u + v + 10)*(su - sv)
            # = sv*(1 - su)*(su - sv) + (su^2 + u + v + 10)*(su - sv)
            # = (su - sv) * (su^2 + u + v + 10 - sv*(su - 1))
            # For the determinant to be non-zero, we need:
            # su != sv AND su^2 + u + v + 10 != sv*(su - 1)
            # Since u, v >= 1, su^2 + u + v + 10 >= 1 + 1 + 1 + 10 = 13.
            # The maximum value of sv*(su - 1) is 3*(3 - 1) = 6.
            # Thus, su^2 + u + v + 10 > sv*(su - 1) is always true.
            # So the condition simplifies to just su != sv.
            if su != sv:
                valid_pair[su][sv] = True
                
    # We want to find the lexicographically smallest valid assignment
    # which corresponds to the minimum V_n.
    # Since V_i = 4*V_{i-1} + s_i, minimizing V_n is equivalent to 
    # finding the lexicographically smallest sequence (s_1, s_2, ..., s_n).
    
    # We use a DP where dp[mask] stores the lexicographically smallest
    # valid assignment for the set of nodes in `mask`.
    # dp[mask] is a tuple of assigned values, or None if impossible.
    dp = [None] * (1 << n)
    dp[0] = ()
    
    for mask in range(1 << n):
        if dp[mask] is None:
            continue
        for i in range(n):
            if not (mask & (1 << i)):
                # Try to assign a value to node i
                for s_i in range(1, 4):
                    ok = True
                    # Check compatibility with already assigned neighbors
                    for j in adj[i]:
                        if mask & (1 << j):
                            # Node j is in the mask, its value is at index popcount(mask & ((1 << j) - 1))
                            j_idx = bin(mask & ((1 << j) - 1)).count('1')
                            s_j = dp[mask][j_idx]
                            if not valid_pair[s_i][s_j]:
                                ok = False
                                break
                    if ok:
                        new_mask = mask | (1 << i)
                        new_tuple = dp[mask] + (s_i,)
                        if dp[new_mask] is None or new_tuple < dp[new_mask]:
                            dp[new_mask] = new_tuple
                            
    full_mask = (1 << n) - 1
    if dp[full_mask] is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, dp[full_mask])))

if __name__ == '__main__':
    solve()