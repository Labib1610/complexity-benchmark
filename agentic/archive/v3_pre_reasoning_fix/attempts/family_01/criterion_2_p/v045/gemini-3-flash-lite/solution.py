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
    # This means for each node i from 1 to n, if not assigned,
    # try assigning 1 first, then 2.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start a BFS/DFS to color the component
            stack = [(i, 1)]
            assignment[i] = 1
            component = []
            
            # Use stack to perform iterative DFS
            comp_stack = [i]
            while comp_stack:
                u = comp_stack.pop()
                component.append(u)
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        comp_stack.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
            # To ensure lexicographically smallest, we must check if
            # swapping 1s and 2s in this component results in a smaller
            # sequence. However, since we process nodes 1..n in order,
            # the first node 'i' of a component MUST be 1 to be lexicographically
            # smallest for that position. If we had picked 2, then 'i' would be 2,
            # which is > 1. So the greedy choice is always valid.
    
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()