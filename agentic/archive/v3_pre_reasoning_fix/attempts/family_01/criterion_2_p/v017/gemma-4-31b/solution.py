import sys

# Increase recursion depth for deep components in large graphs
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # shift[i] = 0 (unassigned), 1 (Shift 1), 2 (Shift 2)
    shift = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence s_1, s_2, ..., s_n,
    # for each connected component, we must decide whether the first 
    # unassigned node in that component should be 1 or 2.
    # Let the component be C. Let u be the smallest node in C.
    # If we assign shift[u] = 1, all other nodes in C are determined.
    # If we assign shift[u] = 2, all other nodes in C are determined.
    # We compare the resulting sequences for C and pick the lexicographically smaller one.
    # Actually, since we want the smallest s_1, s_2, ..., s_n, 
    # we simply try to assign shift[u] = 1 first. 
    # If that leads to a valid 2-coloring, is it always better than shift[u] = 2?
    # Yes, because the first position where the two assignments differ is index u, 
    # and 1 < 2. So we always prefer shift[u] = 1 for the smallest index in each component.
    
    for i in range(1, n + 1):
        if shift[i] == 0:
            # Start BFS/DFS to color the component
            stack = [(i, 1)]
            shift[i] = 1
            component = [i]
            
            # Using a list as a stack for iterative DFS to avoid recursion limits
            idx = 0
            while idx < len(component):
                u = component[idx]
                idx += 1
                
                current_shift = shift[u]
                next_shift = 2 if current_shift == 1 else 1
                
                for v in adj[u]:
                    if shift[v] == 0:
                        shift[v] = next_shift
                        component.append(v)
                    elif shift[v] == current_shift:
                        print("NO")
                        return
    
    print("YES")
    print(*(shift[1:]))

if __name__ == "__main__":
    solve()