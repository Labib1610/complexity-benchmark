import sys

# Increase recursion depth for deep DFS in large graphs
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
        idx += 2
        if u == v:
            # Self-loop makes it impossible to have different frequencies
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    # color[i] will store the assigned frequency (1 or 2)
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, for each connected component,
    # we want to assign the smallest possible value to the smallest index in that component.
    # However, once the first node in a component is assigned a value, the rest are fixed.
    # So for each component, we try assigning '1' to the node with the smallest index.
    # But wait, that's not entirely correct. We need to check if assigning '1' to the 
    # smallest index is possible (it always is if the component is bipartite), 
    # and then see if that leads to the lexicographically smallest result.
    # Actually, for a bipartite component, there are only two valid colorings (swapping 1 and 2).
    # To get the lexicographically smallest sequence, we compare the two possible colorings
    # and pick the one that is lexicographically smaller.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            component = []
            stack = [i]
            color[i] = 1
            component.append(i)
            
            # BFS/DFS to find all nodes in the component and check bipartiteness
            # Using a stack for iterative DFS to avoid recursion limit issues
            visited_idx = 0
            queue = [i]
            while visited_idx < len(queue):
                u = queue[visited_idx]
                visited_idx += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # Now we have a valid 2-coloring for this component.
            # We need to decide if we keep it or flip it (1->2, 2->1).
            # To get the lexicographically smallest sequence, we look at the 
            # smallest index in this component. We want that index to be 1.
            # Since we started the traversal from 'i' (the smallest index in the component)
            # and assigned color[i] = 1, this already minimizes the sequence at the 
            # first possible position.
            # Thus, the current assignment for this component is already the lexicographically smallest.
            
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()