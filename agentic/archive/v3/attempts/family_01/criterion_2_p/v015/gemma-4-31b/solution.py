import sys

# Increase recursion depth for deep DFS in large components
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

    # sector[i] will be 0 (unvisited), 1, or 2
    sector = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence (s1, s2, ..., sn),
    # we process each connected component. For each component, we want the 
    # smallest possible values for the smallest indices.
    # In a bipartite graph, once the color of one node in a component is fixed, 
    # the colors of all other nodes in that component are determined.
    # For a component, there are only two possible valid 2-colorings (swapping 1 and 2).
    # To minimize (s1, s2, ..., sn), we should check which of the two colorings
    # gives a smaller sequence. Specifically, the node with the smallest index
    # in the component should be assigned to sector 1 if possible.
    
    for i in range(1, n + 1):
        if sector[i] == 0:
            # Start a BFS/DFS to color the component
            component = []
            stack = [i]
            sector[i] = 1
            component.append(i)
            
            # Use a stack for DFS to avoid recursion limits and find all nodes in component
            ptr = 0
            queue = [i]
            while ptr < len(queue):
                u = queue[ptr]
                ptr += 1
                for v in adj[u]:
                    if sector[v] == 0:
                        sector[v] = 3 - sector[u]
                        queue.append(v)
                    elif sector[v] == sector[u]:
                        print("NO")
                        return
            
            # Now we have a valid 2-coloring for this component.
            # To make it lexicographically smallest, the node with the smallest index
            # in this component MUST be assigned to 1 if possible.
            # Since we started the traversal from 'i' (the smallest index in the component)
            # and assigned sector[i] = 1, this is already the lexicographically smallest
            # assignment for this component.
            # Wait, that's correct because if we flipped all 1s to 2s and 2s to 1s,
            # the value at index 'i' would become 2, which is > 1.
            
    print("YES")
    print(*(sector[1:]))

if __name__ == "__main__":
    solve()