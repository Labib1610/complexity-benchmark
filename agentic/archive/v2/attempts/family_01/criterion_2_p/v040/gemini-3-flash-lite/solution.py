import sys

# Increase recursion depth for deep DFS trees
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
    
    # We want lexicographically smallest, so try assigning 1 whenever possible
    # We must process components independently.
    # To get lexicographically smallest, for each component, we try setting the first
    # unvisited node to 1, then propagate. If that fails, it's impossible.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # New component
            stack = [(i, 1)]
            assignment[i] = 1
            component = []
            
            # BFS/DFS to find all nodes in this component and assign them
            # To ensure lexicographical smallest, we use a stack but sort neighbors
            # Actually, simply processing 1 to n and assigning 1 whenever possible
            # works because the choice at each step is greedy.
            
            q = [i]
            assignment[i] = 1
            idx_q = 0
            while idx_q < len(q):
                u = q[idx_q]
                idx_q += 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        q.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
                        
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()