import sys

# Increase recursion depth to accommodate deep recursion trees
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

    # Adjacency list: adj[u] contains neighbors v such that v > u
    # This ensures that when we are at node u, we only need to update forward neighbors
    # This optimization reduces the number of checks and updates
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            if u < v:
                adj[u].append(v)
            else:
                adj[v].append(u)
        except StopIteration:
            break

    # colors[i] stores the assigned channel for node i (1, 2, 3)
    # 0 indicates unassigned
    colors = [0] * (n + 1)
    
    # forbidden[i] is a bitmask representing colors forbidden for node i
    # bit 1 corresponds to color 1, bit 2 to color 2, bit 3 to color 3
    # forbidden[i] == 7 (binary 111) means node i cannot be colored
    forbidden = [0] * (n + 1)
    
    # Depth-First Search with backtracking and forward checking
    def dfs(u):
        # If we have assigned colors to all nodes, we found a valid assignment
        if u > n:
            return True
        
        # If the current node is already blocked (all 3 colors forbidden by predecessors)
        if forbidden[u] == 7:
            return False
        
        # Try assigning channels 1, 2, 3 to node u in lexicographical order
        for c in range(1, 4):
            # Check if channel c is available for node u
            if not (forbidden[u] & (1 << c)):
                colors[u] = c
                
                # Forward checking: update forbidden colors for neighbors
                # We record updates to backtrack efficiently
                updates = []
                valid = True
                
                for v in adj[u]:
                    # Check if color c was already forbidden for v
                    was_set = (forbidden[v] & (1 << c))
                    forbidden[v] |= (1 << c)
                    
                    # If v becomes blocked, this branch is invalid
                    if forbidden[v] == 7:
                        valid = False
                        break
                    
                    updates.append((v, was_set))
                
                # If valid so far, recurse
                if valid:
                    if dfs(u + 1):
                        return True
                
                # Backtrack: revert forbidden updates
                # Iterate in reverse order to revert in LIFO manner
                for i in range(len(updates) - 1, -1, -1):
                    v, was_set = updates[i]
                    if not was_set:
                        forbidden[v] &= ~(1 << c)
                
                # Reset color for u
                colors[u] = 0
        
        return False

    # Start DFS from node 1
    if dfs(1):
        print("YES")
        # Output the assigned channels for nodes 1 to n
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()