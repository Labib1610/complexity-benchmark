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
    
    def backtrack(u):
        if u == n:
            return True
        
        # Try assigning 1, 2, 3 to staff member u+1
        # To satisfy lexicographical requirement, we try 1, 2, 3 in order
        for block in [1, 2, 3]:
            can_assign = True
            for prev in range(u):
                if (adj[u + 1] & (1 << prev)):
                    if assignment[prev] == block:
                        can_assign = False
                        break
            
            if can_assign:
                assignment[u] = block
                if backtrack(u + 1):
                    return True
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()