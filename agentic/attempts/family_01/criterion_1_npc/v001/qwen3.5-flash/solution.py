import sys

# Increase recursion depth to handle depth up to N=40 safely, though default is usually sufficient.
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # blocked[i] is a bitmask of colors forbidden for node i by its assigned neighbors
    # Colors are 1, 2, 3 mapped to bits 0, 1, 2 respectively.
    blocked = [0] * (n + 1)
    # assignment array to store the result
    assignment = [0] * (n + 1)
    
    # Recursive backtracking function
    def backtrack(idx):
        # If we have assigned all personnel, we found a valid assignment
        if idx > n:
            return True
        
        # Try to assign colors 1, 2, 3 to node idx in increasing order
        # to ensure lexicographically smallest solution.
        for c in range(1, 4):
            c_bit = 1 << (c - 1)
            
            # Check if color c is allowed for idx (not used by already assigned neighbors)
            if blocked[idx] & c_bit:
                continue
            
            # Tentatively assign c to idx.
            # We need to update the blocked status for neighbors.
            # We only care about neighbors v > idx because neighbors v < idx are already assigned
            # and their validity is checked when they were assigned (or by checking blocked[idx]).
            # If assigning c to idx makes any neighbor v > idx impossible (blocked[v] == 7), we prune.
            
            changes = []
            possible = True
            
            for v in adj[idx]:
                if v > idx:
                    # If c_bit is already blocked for v, blocked[v] doesn't change.
                    # We only need to update if it wasn't blocked.
                    if not (blocked[v] & c_bit):
                        blocked[v] |= c_bit
                        # If blocked[v] becomes 7 (111 binary), it means all 3 colors are forbidden
                        # by assigned neighbors. Since v is unassigned (v > idx), this is a dead end.
                        if blocked[v] == 7:
                            possible = False
                            break
                        changes.append(v)
            
            if possible:
                assignment[idx] = c
                if backtrack(idx + 1):
                    return True
                assignment[idx] = 0 # Backtrack assignment
            
            # Rollback changes to blocked array
            for v in changes:
                blocked[v] &= ~c_bit
                
        return False

    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        # Print the assignment sequence
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()