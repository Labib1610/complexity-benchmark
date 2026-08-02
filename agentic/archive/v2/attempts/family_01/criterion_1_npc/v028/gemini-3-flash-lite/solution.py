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
        v = int(input_data[idx+1])
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
        idx += 2
        
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        
        # Try vault 1, 2, 3 in order for lexicographical smallest
        for vault in [1, 2, 3]:
            # Check if any incompatible neighbor already has this vault
            possible = True
            for prev in range(idx):
                if (adj[idx + 1] & (1 << prev)):
                    if assignment[prev] == vault:
                        possible = False
                        break
            
            if possible:
                assignment[idx] = vault
                if backtrack(idx + 1):
                    return True
        return False

    # The constraint n <= 40 is small enough for backtracking with pruning 
    # if the graph is sparse or constraints are tight. 
    # For general 3-coloring, it's NP-hard, but 40 is small.
    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()