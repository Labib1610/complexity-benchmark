import sys

sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    assignment = [0] * n
    forbidden = [0] * n  # Bitmask: bit i means shift (i+1) is forbidden
    
    def backtrack(worker):
        if worker == n:
            return True
        
        for shift in range(1, 4):
            if forbidden[worker] & (1 << (shift - 1)):
                continue
            
            assignment[worker] = shift
            
            # Update forbidden for unassigned neighbors
            for neighbor in adj[worker]:
                if assignment[neighbor] == 0:
                    forbidden[neighbor] |= (1 << (shift - 1))
            
            # Forward checking
            possible = True
            for j in range(worker + 1, n):
                if forbidden[j] == 7:  # All shifts forbidden
                    possible = False
                    break
            
            if possible and backtrack(worker + 1):
                return True
            
            # Undo
            for neighbor in adj[worker]:
                if assignment[neighbor] == 0:
                    forbidden[neighbor] &= ~(1 << (shift - 1))
            assignment[worker] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()