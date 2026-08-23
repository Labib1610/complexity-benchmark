import sys

# Increase recursion depth just in case
sys.setrecursionlimit(5000)

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    iterator = iter(data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # avail[u] is a bitmask of available colors for node u
    # Colors are 1, 2, 3 mapped to bits 0, 1, 2
    # Initially all 3 colors available: 111 binary = 7
    avail = [7] * n
    assignment = [0] * n
    
    # To optimize, we can check if the graph is 3-colorable quickly?
    # For N=40, forward checking is usually sufficient.
    
    def backtrack(u):
        if u == n:
            return True
        
        # Try colors 1, 2, 3 in order
        for c in range(1, 4):
            # Check if color c is available for u
            # c=1 -> bit 0 (1), c=2 -> bit 1 (2), c=3 -> bit 2 (4)
            bit = 1 << (c - 1)
            
            if not (avail[u] & bit):
                continue
            
            # Forward checking: Check if assigning c to u makes any neighbor v > u have 0 options
            # We only need to check neighbors v > u because neighbors v < u are already assigned
            # and their constraints are already reflected in avail[u].
            # For v > u, we need to check if removing c from avail[v] makes it 0.
            # This happens if avail[v] == bit exactly.
            
            can_assign = True
            affected_neighbors = []
            
            for v in adj[u]:
                if v > u:
                    if avail[v] == bit:
                        can_assign = False
                        break
                    else:
                        affected_neighbors.append(v)
            
            if not can_assign:
                continue
            
            # Assign
            assignment[u] = c
            for v in affected_neighbors:
                avail[v] &= ~bit
            
            if backtrack(u + 1):
                return True
            
            # Backtrack
            for v in affected_neighbors:
                avail[v] |= bit
            assignment[u] = 0
            
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()