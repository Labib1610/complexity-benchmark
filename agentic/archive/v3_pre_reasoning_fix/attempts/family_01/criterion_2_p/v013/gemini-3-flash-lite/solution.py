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
    # where si is 1 or 2. We prefer 1 over 2.
    # This is a 2-coloring problem.
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Try setting to 1 (smallest)
            stack = [(i, 1)]
            assignment[i] = 1
            
            # Use a list to store nodes in this component for backtracking if needed
            component = []
            
            while stack:
                u, color = stack.pop()
                component.append(u)
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - color
                        stack.append((v, 3 - color))
                    elif assignment[v] == color:
                        print("NO")
                        return
    
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()