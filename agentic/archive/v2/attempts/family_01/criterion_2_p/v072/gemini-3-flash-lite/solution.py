import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(300000)

def solve():
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
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
    
    # We want the lexicographically smallest assignment.
    # This means we prefer s_i = 1 whenever possible.
    # If a component is bipartite, we have two colorings (swapping 1s and 2s).
    # To get the lexicographically smallest, for each component, we check
    # which coloring results in a smaller value for the first node encountered.
    
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # BFS/DFS to find all nodes in this component
            component = []
            stack = [i]
            assignment[i] = 1
            component.append(i)
            
            # Use a list to store the component nodes
            idx_comp = 0
            while idx_comp < len(component):
                u = component[idx_comp]
                idx_comp += 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        component.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
            # Check if swapping 1s and 2s makes it lexicographically smaller
            # We only care about the smallest index 'i' in this component.
            # If assignment[i] == 2, swapping will make assignment[i] = 1,
            # which is better.
            if assignment[i] == 2:
                for node in component:
                    assignment[node] = 3 - assignment[node]
    
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()