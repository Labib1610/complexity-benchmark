import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        idx += 2
        
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        
        # Try vaults 1, 2, 3 in order to get lexicographical smallest
        for v in range(1, 4):
            can_place = True
            for prev in range(idx):
                if (adj[idx] & (1 << prev)) and assignment[prev] == v:
                    can_place = False
                    break
            
            if can_place:
                assignment[idx] = v
                if backtrack(idx + 1):
                    return True
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()