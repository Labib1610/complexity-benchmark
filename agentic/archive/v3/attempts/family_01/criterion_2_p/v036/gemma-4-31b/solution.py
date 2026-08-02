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
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
    
    # assignment[i] will be 0 (unassigned), 1 (Zone 1), or 2 (Zone 2)
    assignment = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we process nodes in order from 1 to n.
    # For each connected component, the first node we encounter (the smallest index)
    # should be assigned to Zone 1 if possible.
    # Since the bipartite coloring is unique up to flipping colors within a component,
    # assigning the first node of a component to 1 and then propagating the colors
    # will always yield the lexicographically smallest result for that component.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS to color this component
            # Start with Zone 1 for the smallest index in the component
            assignment[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                current_color = assignment[u]
                next_color = 2 if current_color == 1 else 1
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = next_color
                        stack.append(v)
                    elif assignment[v] == current_color:
                        print("NO")
                        return
    
    # If we reached here, it's bipartite
    print("YES")
    print(*(assignment[1:]))

if __name__ == "__main__":
    solve()