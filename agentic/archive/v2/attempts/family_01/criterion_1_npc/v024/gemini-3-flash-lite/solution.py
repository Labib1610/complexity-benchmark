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
    
    def backtrack(k):
        if k == n:
            return True
        
        # Try vaults 1, 2, 3 in order to ensure lexicographical smallest
        for vault in range(1, 4):
            can_place = True
            for i in range(k):
                if (adj[k + 1] & (1 << i)):
                    if assignment[i] == vault:
                        can_place = False
                        break
            
            if can_place:
                assignment[k] = vault
                if backtrack(k + 1):
                    return True
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()