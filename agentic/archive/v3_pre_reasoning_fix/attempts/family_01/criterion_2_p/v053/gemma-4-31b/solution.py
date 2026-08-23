import sys

# Increase recursion depth for deep DFS in bipartite check
sys.setrecursionlimit(300000)

def solve():
    # Read n and m
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

    # color[i] will be 0 (unvisited), 1 (Bus 1), or 2 (Bus 2)
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment:
    # For each connected component, we want to assign the smallest possible values
    # to the smallest indices. 
    # Since we only have two choices for the first node of a component (1 or 2),
    # and that choice determines the colors of all other nodes in the component,
    # we check if starting with 1 is valid and if it results in a smaller sequence.
    
    # Actually, the rule is simpler: for each connected component, 
    # we must determine whether starting the first node (the one with the smallest index) 
    # with 1 or 2 leads to a lexicographically smaller result.
    # Let's say the first node in the component is 'root'.
    # If we set color[root] = 1, the other nodes are fixed.
    # If we set color[root] = 2, the other nodes are swapped (1->2, 2->1).
    # To be lexicographically smallest, we want the smallest index in the component
    # to have the smallest possible value (1).
    # If we can set the smallest index to 1, we should. 
    # This will always be lexicographically smaller than setting it to 2.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start a BFS/DFS to color the component
            stack = [i]
            color[i] = 1 # Try assigning the smallest available bus to the smallest index
            component = [i]
            
            # Using iterative DFS to avoid recursion depth issues and find all nodes in component
            ptr = 0
            while ptr < len(component):
                u = component[ptr]
                ptr += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()