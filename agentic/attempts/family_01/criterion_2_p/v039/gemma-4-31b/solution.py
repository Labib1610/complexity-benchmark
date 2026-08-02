import sys

# Increase recursion depth for deep DFS trees in large components
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
            # A researcher cannot be restricted with themselves
            # because they must be in one of the two labs.
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    # color[i] will be 0 (unvisited), 1, or 2
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, 
    # we process researchers from 1 to n.
    # For each connected component, we want the smallest possible 
    # values for the smallest indices.
    # In a bipartite component, if we fix the color of one node, 
    # the colors of all other nodes in that component are determined.
    # Let the component be C. Let v_min be the smallest index in C.
    # We should try setting color[v_min] = 1 first. 
    # Then we check if this leads to a lexicographically smaller sequence 
    # compared to color[v_min] = 2.
    # Actually, for a bipartite component, once we fix the color of the 
    # smallest index v_min as 1, we get a sequence. If we fix it as 2, 
    # every node in the component flips 1 <-> 2.
    # The sequence is lexicographically smaller if the first index 
    # where the two assignments differ has a '1' in the first sequence.
    # Since v_min is the first index that differs, setting color[v_min] = 1 
    # always results in a lexicographically smaller assignment for that component.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS to color the component
            # Using a stack for iterative DFS to avoid recursion limits and for speed
            stack = [i]
            color[i] = 1
            component = []
            
            # Standard bipartite check using DFS
            # We use a manual stack to simulate DFS
            q = [i]
            visited_in_comp = {i}
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                component.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()