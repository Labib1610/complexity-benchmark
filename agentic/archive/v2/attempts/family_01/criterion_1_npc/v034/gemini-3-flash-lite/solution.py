import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
        idx += 2
        
    assignment = [0] * n
    
    def backtrack(curr):
        if curr == n:
            return True
        
        # Try assigning 1, then 2, then 3 for the current staff member
        for time_block in range(1, 4):
            # Check compatibility
            possible = True
            for prev in range(curr):
                if (adj[curr + 1] & (1 << prev)):
                    if assignment[prev] == time_block:
                        possible = False
                        break
            
            if possible:
                assignment[curr] = time_block
                if backtrack(curr + 1):
                    return True
        
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()