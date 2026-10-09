import sys

# Increase recursion depth for DFS
sys.setrecursionlimit(500000)

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Colors: 0 = uncolored, 1 = flag 1, 2 = flag 2
    colors = [0] * (n + 1)
    
    # We iterate through nodes 1 to n.
    # If a node is uncolored, we start a DFS to color its connected component.
    # We always try to assign color 1 first to satisfy the lexicographical requirement.
    possible = True
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start DFS for this component
            # We use a stack to simulate recursion to avoid RecursionError or stack overflow
            # though sys.setrecursionlimit usually handles 2*10^5 depth in CP environments if not too deep.
            # However, a linear chain graph could have depth n. Stack simulation is safer.
            
            stack = [i]
            colors[i] = 1
            
            while stack:
                u = stack.pop()
                
                for v in adj[u]:
                    if colors[v] == 0:
                        # Assign the opposite color
                        # If u is 1, v must be 2. If u is 2, v must be 1.
                        colors[v] = 3 - colors[u]
                        stack.append(v)
                    elif colors[v] == colors[u]:
                        # Conflict found
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break

    if not possible:
        print("NO")
    else:
        print("YES")
        # Print colors 1 to n, space-separated
        output_str = " ".join(map(str, colors[1:n+1]))
        print(output_str)

if __name__ == '__main__':
    solve()