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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    # We want lexicographically smallest assignment.
    # This means we prefer 1 over 2 for each i from 1 to n.
    # This is a standard 2-coloring problem.
    # Since we want lexicographically smallest, we iterate 1 to n.
    # If a node is unvisited, we try assigning it '1' and propagate.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for this connected component
            stack = [(i, 1)]
            assignment[i] = 1
            component = []
            
            # Use stack to avoid recursion depth issues and manage traversal
            q = [i]
            assignment[i] = 1
            visited_order = [i]
            
            head = 0
            while head < len(visited_order):
                u = visited_order[head]
                head += 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        visited_order.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(assignment[1:]))

solve()