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
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # color[i] will be 0 if unvisited, 1 or 2 if assigned to a bus line
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we process components
    # in order of their smallest node index. For each component, we try 
    # assigning the smallest node to 1. If that works, we check if 
    # swapping 1 <-> 2 in that component would result in a lexicographically 
    # smaller sequence.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            component = []
            stack = [i]
            color[i] = 1
            
            # Iterative DFS to avoid recursion limits and find all nodes in component
            q = [i]
            idx = 0
            while idx < len(q):
                u = q[idx]
                idx += 1
                component.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # For the current component, we have a valid 2-coloring.
            # There are only two possibilities: the current coloring or the flipped one.
            # To get the lexicographically smallest sequence, we compare the two.
            # We only need to check the smallest index in the component.
            # However, the smallest index is always 'i' because we iterate i from 1 to n.
            # If we set color[i] = 1, it's always better or equal than color[i] = 2.
            # Thus, the current coloring (where color[i] = 1) is already the best.
            # Wait, that's only true if the smallest index in the component is i.
            # Since we iterate i from 1 to n and only start DFS if color[i] == 0,
            # i is indeed the smallest index in the component.
            # Therefore, setting color[i] = 1 is always optimal for lexicographical order.
            pass

    print("YES")
    print(*(color[1:]))

if __name__ == "__main__":
    solve()