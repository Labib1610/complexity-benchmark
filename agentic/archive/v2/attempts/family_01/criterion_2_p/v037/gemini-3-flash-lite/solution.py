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
        v = int(input_data[idx+1])
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    assignment = [0] * (n + 1)
    
    # To get the lexicographically smallest, we iterate 1 to n.
    # If a component is not yet colored, try assigning 1 first (greedy).
    for i in range(1, n + 1):
        if assignment[i] == 0:
            stack = [(i, 1)]
            assignment[i] = 1
            while stack:
                u, color = stack.pop()
                next_color = 2 if color == 1 else 1
                
                # To maintain lexicographical order within a component,
                # we process neighbors. However, standard 2-coloring
                # is fixed once the first node in the component is set.
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = next_color
                        stack.append((v, next_color))
                    elif assignment[v] == color:
                        print("NO")
                        return
                        
    print("YES")
    print(*(assignment[1:]))

solve()