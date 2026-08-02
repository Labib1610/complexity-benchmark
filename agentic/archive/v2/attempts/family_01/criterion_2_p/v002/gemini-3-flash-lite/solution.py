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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    # We want the lexicographically smallest sequence.
    # This means for each connected component, we try to assign 1 to the smallest 
    # available node, and then propagate.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS from i, assign 1 to i
            stack = [i]
            assignment[i] = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        stack.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
                        
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()