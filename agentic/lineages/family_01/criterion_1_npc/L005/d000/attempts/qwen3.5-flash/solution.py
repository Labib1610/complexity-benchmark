import sys

# Increase recursion depth to handle deep recursion if necessary.
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
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
    # We only store edges (u, v) where u < v to optimize processing
    # This way, when at node u, we only update neighbors v > u (unassigned nodes)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u > v:
            u, v = v, u
        adj[u].append(v)

    # allowed[u] stores a bitmask of allowed colors for node u
    # Colors are 1, 2, 3 corresponding to bits 0, 1, 2
    # Initial value 7 (binary 111) means all colors are allowed
    allowed = [7] * (n + 1)
    
    # assignment[u] stores the color assigned to node u
    assignment = [0] * (n + 1)

    # DFS to find the lexicographically smallest valid 3-coloring
    def dfs(u):
        # If we have assigned colors to all nodes, we found a solution
        if u > n:
            return True
        
        # If current node has no allowed colors, this path is invalid
        if allowed[u] == 0:
            return False
        
        # Try to assign colors 1, 2, 3 to node u
        # We iterate in order 1, 2, 3 to ensure lexicographically smallest result
        # Colors correspond to bitmasks 1, 2, 4
        for color_bit in [1, 2, 4]:
            if (allowed[u] & color_bit):
                # This color is available for u
                # We need to tentatively assign it and check validity for neighbors
                
                changes = []
                possible = True
                
                # Update allowed colors for neighbors
                for v in adj[u]:
                    old_allowed = allowed[v]
                    new_allowed = old_allowed & ~color_bit
                    allowed[v] = new_allowed
                    changes.append((v, old_allowed))
                    
                    # If a neighbor has no allowed colors left, this assignment is invalid
                    if new_allowed == 0:
                        possible = False
                        # We stop updating neighbors to save time, 
                        # but we must rollback the changes we already made
                        break
                
                if possible:
                    assignment[u] = color_bit.bit_length() # 1->1, 2->2, 4->3
                    if dfs(u + 1):
                        return True
                    # Backtrack assignment
                    assignment[u] = 0
                
                # Rollback changes to allowed array
                for v, old_allowed in changes:
                    allowed[v] = old_allowed
                    
        return False

    if dfs(1):
        print("YES")
        # Print the assignment sequence for nodes 1 to n
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()