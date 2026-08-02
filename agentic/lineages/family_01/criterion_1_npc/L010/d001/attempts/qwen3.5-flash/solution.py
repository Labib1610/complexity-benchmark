import sys

# Increase recursion depth to accommodate deep recursion trees if necessary
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
    # Using 1-based indexing for tasks
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # colors array to store assigned tiers (1, 2, 3)
    # 0 indicates unassigned
    colors = [0] * (n + 1)
    
    # masks array to store available colors for unassigned nodes
    # Bitmask: bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    # Value 7 (111 binary) means all colors available
    masks = [7] * (n + 1)

    # Function to perform backtracking with forward checking
    def backtrack(idx):
        # If all tasks are assigned (1 to n)
        if idx > n:
            return list(colors[1:])
        
        # Try assigning tiers 1, 2, 3 in order to ensure lexicographically smallest sequence
        for c in [1, 2, 3]:
            c_bit = 1 << (c - 1)
            
            # Check if assigning color c to task idx is valid
            # It must not conflict with any already assigned neighbor
            conflict = False
            for v in adj[idx]:
                if colors[v] == c:
                    conflict = True
                    break
            if conflict:
                continue
            
            # If valid, update masks for unassigned neighbors
            # Unassigned neighbors are those with colors[v] == 0
            # Since we assign in order 1..n, unassigned neighbors will have v > idx
            changed_masks = []
            ok = True
            
            for v in adj[idx]:
                if colors[v] == 0:
                    # Remove color c from available colors for v
                    masks[v] &= ~c_bit
                    
                    # If no colors left for v, this branch is invalid (forward checking)
                    if masks[v] == 0:
                        ok = False
                        changed_masks.append(v)
                        break
                    
                    changed_masks.append(v)
            
            if not ok:
                # Backtrack: restore masks
                for v in changed_masks:
                    masks[v] |= c_bit
                continue
            
            # Tentatively assign color
            colors[idx] = c
            
            # Recurse to the next task
            result = backtrack(idx + 1)
            if result is not None:
                return result
            
            # Backtrack: restore state
            colors[idx] = 0
            for v in changed_masks:
                masks[v] |= c_bit
                
        return None

    # Start backtracking from task 1
    solution = backtrack(1)
    
    if solution:
        print("YES")
        print(*(solution))
    else:
        print("NO")

if __name__ == '__main__':
    solve()