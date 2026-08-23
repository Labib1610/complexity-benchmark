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
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    def backtrack(unit):
        if unit > n:
            return True
        
        # Try blocks 1, 2, 3 in order to find the lexicographically smallest assignment
        for color in range(1, 4):
            can_assign = True
            # Check constraints with already assigned units
            for prev in range(1, unit):
                if (adj[unit] & (1 << prev)) and assignment[prev] == color:
                    can_assign = False
                    break
            
            if can_assign:
                assignment[unit] = color
                if backtrack(unit + 1):
                    return True
                assignment[unit] = 0
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()