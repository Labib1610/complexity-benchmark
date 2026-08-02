import sys
from collections import deque

# Increase recursion depth to handle deep recursion if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # allowed[u] is a bitmask of allowed colors for vertex u
    # 1 -> color 1 (bit 0)
    # 2 -> color 2 (bit 1)
    # 4 -> color 3 (bit 2)
    # Initial state: all colors allowed (1 | 2 | 4 = 7)
    allowed = [7] * (n + 1)
    
    # Helper to check if a value has exactly 1 bit set
    def has_one_bit(val):
        return val > 0 and (val & (val - 1)) == 0
    
    # Helper to check if a value has 0 bits set
    def has_zero_bits(val):
        return val == 0

    # Propagate constraints. Returns True if valid, False if contradiction
    def propagate(current_allowed):
        q = deque()
        # Initialize queue with all vertices that have exactly one allowed color
        for i in range(1, n + 1):
            if has_one_bit(current_allowed[i]):
                q.append(i)
            elif has_zero_bits(current_allowed[i]):
                return False # Contradiction found immediately

        while q:
            u = q.popleft()
            c = current_allowed[u] # c is the mask of the single allowed color (1, 2, or 4)
            
            for v in adj[u]:
                # Remove the color c from v's allowed set
                current_allowed[v] &= ~c
                if has_zero_bits(current_allowed[v]):
                    return False
                if has_one_bit(current_allowed[v]):
                    # If v now has only one allowed color, add to queue to propagate further
                    q.append(v)
        
        return True

    # Recursive backtracking function
    def backtrack(current_allowed):
        # Find the first vertex with more than 1 allowed color
        # This is the next vertex we need to make a decision for (to maintain lexicographical order)
        # Vertices with 1 allowed color are forced and skipped.
        # Vertices with 0 allowed color imply failure (handled in propagation, but check here too).
        
        first_unassigned = -1
        for i in range(1, n + 1):
            if not has_one_bit(current_allowed[i]) and not has_zero_bits(current_allowed[i]):
                first_unassigned = i
                break
        
        # If no vertex has > 1 allowed color
        if first_unassigned == -1:
            # Check if any vertex has 0 allowed color (contradiction)
            for i in range(1, n + 1):
                if has_zero_bits(current_allowed[i]):
                    return False
            # All vertices have exactly 1 allowed color -> Solution found
            return True

        # If we found a vertex to assign
        u = first_unassigned
        
        # Try colors 1, 2, 3 in order
        # Colors correspond to bits 1, 2, 4
        for c in [1, 2, 4]:
            if (current_allowed[u] & c):
                # Create a copy of the state
                next_allowed = current_allowed[:]
                
                # Assign color c to u
                next_allowed[u] = c
                
                # Propagate constraints
                if propagate(next_allowed):
                    # If propagation succeeds, recurse
                    if backtrack(next_allowed):
                        return True
        
        return False

    # Start the search
    if backtrack(allowed):
        print("YES")
        # Construct the solution from the allowed masks
        # Since we found a solution, every vertex has exactly 1 bit set
        s = []
        for i in range(1, n + 1):
            if allowed[i] == 1:
                s.append(1)
            elif allowed[i] == 2:
                s.append(2)
            elif allowed[i] == 4:
                s.append(3)
        print(*(s))
    else:
        print("NO")

if __name__ == '__main__':
    solve()