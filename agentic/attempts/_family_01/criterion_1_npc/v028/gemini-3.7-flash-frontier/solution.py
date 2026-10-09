import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    degree = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v and not (adj[u] & (1 << v)):
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            degree[u] += 1
            degree[v] += 1

    color = [-1] * n
    available = [7] * n  # bits 0, 1, 2 represent colors 0, 1, 2

    # Precompute popcount for 0..7
    popcnt = [bin(i).count('1') for i in range(8)]

    def backtrack(assigned_count):
        if assigned_count == n:
            return True

        # Select unassigned vertex with minimum available colors (MRV)
        # Tie-break by highest degree
        best_v = -1
        best_cnt = 4
        best_deg = -1

        for i in range(n):
            if color[i] == -1:
                cnt = popcnt[available[i]]
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_deg = degree[i]
                    best_v = i
                    if cnt <= 1:
                        break
                elif cnt == best_cnt:
                    if degree[i] > best_deg:
                        best_deg = degree[i]
                        best_v = i

        if best_cnt == 0:
            return False

        u = best_v
        mask = available[u]

        # Try each available color
        for c in range(3):
            if (mask & (1 << c)):
                color[u] = c
                
                # Forward checking
                # Save affected neighbors to undo
                affected = []
                c_mask = 1 << c
                adj_u = adj[u]
                
                # Check neighbors
                temp_adj = adj_u
                while temp_adj > 0:
                    lsb = temp_adj & -temp_adj
                    v = (lsb.bit_length() - 1)
                    temp_adj ^= lsb
                    if color[v] == -1 and (available[v] & c_mask):
                        available[v] &= ~c_mask
                        affected.append(v)
                
                if backtrack(assigned_count + 1):
                    return True
                
                # Undo
                for v in affected:
                    available[v] |= c_mask
                color[u] = -1

        return False

    if backtrack(0):
        print("YES")
        print(*(color[i] + 1 for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()