import sys

# Increase recursion depth for deep graphs
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
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # s[i] will store the channel (1 or 2)
    s = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, for each connected component,
    # we need to decide whether the first unvisited node in that component should be 1 or 2.
    # Since we want the smallest vector (s1, s2, ... sn), we should try setting the 
    # smallest index in each component to 1 if possible.
    # In a bipartite graph, once the color of one node in a component is fixed, 
    # all other colors in that component are determined.
    
    for i in range(1, n + 1):
        if s[i] == 0:
            # Start a BFS/DFS to color this component
            # We want s[i] to be 1 to minimize lexicographically
            stack = [i]
            s[i] = 1
            
            # We use a temporary list to track nodes in the current component
            component = [i]
            ptr = 0
            while ptr < len(component):
                u = component[ptr]
                ptr += 1
                for v in adj[u]:
                    if s[v] == 0:
                        s[v] = 3 - s[u]
                        component.append(v)
                    elif s[v] == s[u]:
                        print("NO")
                        return
            
            # After coloring the component, we check if swapping 1s and 2s 
            # would result in a lexicographically smaller sequence.
            # Since we processed nodes in increasing order of indices,
            # the first node we encountered (i) is the smallest index in the component.
            # Setting s[i] = 1 is always optimal for the lexicographical smallest sequence
            # because any other valid assignment for this component would have s[i] = 2,
            # which is lexicographically larger.
            
    print("YES")
    print(*(s[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()