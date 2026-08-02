import sys

# Increase recursion depth for deep DFS trees in bipartite checking
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
        
    # color[i] will be 0 (unvisited), 1 (Group 1), or 2 (Group 2)
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, for each connected component,
    # we want the smallest possible labels for the smallest indices.
    # Since we only have two choices for a bipartite component (flip all 1s to 2s and vice versa),
    # for each component, we find the smallest index 'v' in that component.
    # We try assigning color[v] = 1. If that works, we check if the resulting 
    # sequence for that component is lexicographically smaller than if we assigned color[v] = 2.
    # Actually, assigning the smallest index in the component to 1 always 
    # helps the sequence be lexicographically smaller, provided the component is bipartite.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start a BFS/DFS to color the component
            component = []
            stack = [i]
            color[i] = 1
            
            # Use a simple iterative BFS/DFS to avoid recursion limit and find all nodes in component
            visited_in_comp = []
            q = [i]
            idx = 0
            while idx < len(q):
                u = q[idx]
                idx += 1
                visited_in_comp.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # Now we have a valid 2-coloring for this component.
            # Let the current coloring be C. The only other valid coloring is C' (where 1 <-> 2).
            # To make the sequence (s_1, s_2, ..., s_n) lexicographically smallest,
            # we look at the smallest index 'min_idx' in this component.
            # If we set color[min_idx] = 1, is it always better than color[min_idx] = 2?
            # Yes, because the first position where the two sequences differ is min_idx.
            # Since 1 < 2, we must have color[min_idx] = 1.
            
            # Find the minimum index in the component
            min_node = min(visited_in_comp)
            if color[min_node] == 2:
                # Flip colors for all nodes in this component
                for node in visited_in_comp:
                    color[node] = 3 - color[node]
                    
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()