import sys

# Increase recursion depth to handle deep recursion if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # colors: 0 = unassigned, 1, 2, 3 = assigned
    # domains: bitmask of available colors. 1=1, 2=2, 4=3. Initially 7 (111).
    
    # Initial state
    colors = [0] * (n + 1)
    domains = [7] * (n + 1)

    # Backtracking function
    def backtrack(idx, colors, domains):
        if idx == n + 1:
            return True
        
        # If current node is already assigned (forced by previous), skip
        if colors[idx] != 0:
            return backtrack(idx + 1, colors, domains)
        
        # If domain is empty, this branch is invalid
        if domains[idx] == 0:
            return False
        
        # Try colors 1, 2, 3 in order
        for c in [1, 2, 3]:
            # Check if c is valid for idx (i.e., in domains[idx])
            if not ((domains[idx] >> (c - 1)) & 1):
                continue
            
            # Create new state (copying)
            new_colors = list(colors)
            new_domains = list(domains)
            
            new_colors[idx] = c
            
            # Propagate constraints
            valid_choice = True
            
            # We use a stack for propagation
            stack = []
            
            # Update neighbors of idx
            for v in adj[idx]:
                if new_colors[v] == 0:
                    new_domains[v] &= ~(1 << (c - 1))
                    if new_domains[v] == 0:
                        valid_choice = False
                        break
                    # Check if forced (domain size 1)
                    if (new_domains[v] & (new_domains[v] - 1)) == 0:
                        stack.append(v)
            
            if valid_choice:
                while stack:
                    u = stack.pop()
                    # If u was already assigned (e.g. added multiple times to stack), skip
                    if new_colors[u] != 0:
                        continue
                    
                    # Determine forced color
                    if new_domains[u] & 1:
                        forced_c = 1
                    elif new_domains[u] & 2:
                        forced_c = 2
                    else:
                        forced_c = 3
                    
                    new_colors[u] = forced_c
                    
                    # Update neighbors of u
                    for w in adj[u]:
                        if new_colors[w] == 0:
                            new_domains[w] &= ~(1 << (forced_c - 1))
                            if new_domains[w] == 0:
                                valid_choice = False
                                break
                            # Check if forced
                            if (new_domains[w] & (new_domains[w] - 1)) == 0:
                                stack.append(w)
                    if not valid_choice:
                        break
            
            if valid_choice:
                if backtrack(idx + 1, new_colors, new_domains):
                    return True
        
        return False

    if backtrack(1, colors, domains):
        print("YES")
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()