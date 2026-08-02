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
    
    # We want the lexicographically smallest assignment (s1, s2, ..., sn)
    # where si in {1, 2}.
    # This is equivalent to 2-coloring.
    # To get the lexicographically smallest, we iterate i from 1 to n.
    # If worker i is unassigned, try assigning 1. If that fails, try 2.
    
    assignment = [0] * (n + 1)
    
    def dfs(u, color):
        assignment[u] = color
        for v in adj[u]:
            if assignment[v] == 0:
                if not dfs(v, 3 - color):
                    return False
            elif assignment[v] == color:
                return False
        return True

    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Try assigning 1 to the current component
            # To ensure lexicographical smallest, we greedily assign 1
            # to the smallest unassigned node and propagate.
            if not dfs(i, 1):
                # If 1 fails, we must reset this component and try 2
                # Resetting is tricky, so we clear the component first
                stack = [i]
                nodes = []
                while stack:
                    curr = stack.pop()
                    if assignment[curr] != 0:
                        assignment[curr] = 0
                        nodes.append(curr)
                        for neighbor in adj[curr]:
                            if assignment[neighbor] != 0:
                                stack.append(neighbor)
                
                # Now try assigning 2
                if not dfs(i, 2):
                    print("NO")
                    return

    print("YES")
    print(*(assignment[1:]))

solve()