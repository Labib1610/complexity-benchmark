import sys

# Increase recursion depth for deep DFS in bipartite checking
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # colors: 0 = unvisited, 1 = shift 1, 2 = shift 2
    colors = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, 
    # for each connected component, we want the smallest index 
    # in that component to be assigned to shift 1 if possible.
    # However, the bipartite coloring is constrained: once the first 
    # node in a component is colored, all others are determined.
    # To minimize lexicographically, we must decide for each component 
    # whether the "color 1" group gets shift 1 and "color 2" gets shift 2, 
    # or vice versa.
    
    # The lexicographically smallest sequence s_1, s_2, ..., s_n is found by 
    # making s_1 as small as possible, then s_2, and so on.
    # For each connected component, let the smallest index be 'root'.
    # We must assign s_{root} = 1. Then all other nodes in that component 
    # are forced.
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS/DFS from i. Since we process i from 1 to n, 
            # i is the smallest index in its component.
            # To minimize lexicographically, we MUST set colors[i] = 1.
            stack = [i]
            colors[i] = 1
            
            # Using iterative DFS to avoid recursion limits and for speed
            visited_in_comp = [i]
            ptr = 0
            while ptr < len(visited_in_comp):
                u = visited_in_comp[ptr]
                ptr += 1
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]
                        visited_in_comp.append(v)
                    elif colors[v] == colors[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(colors[1:]))

if __name__ == "__main__":
    solve()